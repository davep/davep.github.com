---
title: Me vs Claude
date: 2026-05-02 18:48:30+0100
category: AI
tags: BlogMore, Coding, Copilot, GitHub, Python, code review, testing
---

After writing the [earlier
post](/2026/05/02/it-was-such-a-simple-request.html) I had to AFK to attend
to normal life things. When I finally sat back at my keyboard, I decided to
write my own take on `minified_filename`.

To recap, this is what Copilot/Claude came up with first:

```python
def minified_filename(source: str) -> str:
    """Compute the minified output filename for a given source filename.

    Transforms the file extension: ``.css`` becomes ``.min.css`` and
    ``.js`` becomes ``.min.js``.  For example, ``theme.js`` becomes
    ``theme.min.js`` and ``style.css`` becomes ``style.min.css``.

    Args:
        source: Source filename ending in ``.css`` or ``.js``.

    Returns:
        The corresponding minified filename.

    Raises:
        ValueError: If *source* does not end with ``.css`` or ``.js``.
    """
    if source.endswith(".css"):
        return source[: -len(".css")] + ".min.css"
    if source.endswith(".js"):
        return source[: -len(".js")] + ".min.js"
    raise ValueError(f"Unsupported file extension for minification: {source!r}")
```

This is what it arrived at once it had self-reviewed the above:

```python
def minified_filename(source: str) -> str:
    """Compute the minified output filename for a given source filename.

    Transforms the file extension: ``.css`` becomes ``.min.css`` and
    ``.js`` becomes ``.min.js``.  For example, ``theme.js`` becomes
    ``theme.min.js`` and ``style.css`` becomes ``style.min.css``.

    Args:
        source: Source filename ending in ``.css`` or ``.js``.

    Returns:
        The corresponding minified filename.

    Raises:
        ValueError: If *source* does not end with ``.css`` or ``.js``.
    """
    if source.endswith(".css"):
        return source.removesuffix(".css") + ".min.css"
    if source.endswith(".js"):
        return source.removesuffix(".js") + ".min.js"
    raise ValueError(f"Unsupported file extension for minification: {source!r}")
```

The tests it wrote looked like this:

```python
class TestMinifiedFilename:
    """Test the minified_filename utility function."""

    def test_css_extension_becomes_min_css(self) -> None:
        """Test that a .css extension is replaced with .min.css."""
        assert minified_filename("style.css") == "style.min.css"

    def test_js_extension_becomes_min_js(self) -> None:
        """Test that a .js extension is replaced with .min.js."""
        assert minified_filename("theme.js") == "theme.min.js"

    def test_hyphenated_css_filename(self) -> None:
        """Test that a hyphenated CSS filename is handled correctly."""
        assert minified_filename("tag-cloud.css") == "tag-cloud.min.css"

    def test_hyphenated_js_filename(self) -> None:
        """Test that a hyphenated JS filename is handled correctly."""
        assert minified_filename("search.js") == "search.min.js"

    def test_unsupported_extension_raises(self) -> None:
        """Test that an unsupported extension raises ValueError."""
        with pytest.raises(ValueError, match="Unsupported file extension"):
            minified_filename("style.txt")
```

I wasn't too keen on the obsession with just `.css` and `.js` files (it
seemed unnecessary), and neither did I like the hard-coding of the resulting
extensions, etc. It all felt too job-specific.

So my take on the code was this:

```python
def minified_filename(source: str | Path) -> str:
    """Compute the minified output filename for a given source filename.

    Args:
        source: Source filename.

    Returns:
        The corresponding minified filename.
    """
    if isinstance(source, str) and not source:
        return source
    if (source := Path(source)).suffix:
        source = source.with_suffix(f".min{source.suffix}")
    return str(source)
```

The tests being this:

```python
class TestMinifiedFilename:
    """Test the minified_filename utility function."""

    @pytest.mark.parametrize(
        "before,after",
        [
            ("style.css", "style.min.css"),
            ("theme.js", "theme.min.js"),
            ("style.min.css", "style.min.min.css"),
            ("file", "file"),
            (".file", ".file"),
            (".file.css", ".file.min.css"),
            ("", ""),
        ],
    )
    def test_min_file(self, before: str, after: str) -> None:
        """Test that converting a filename to the minified version has the expected effect."""
        assert minified_filename(before) == after
```

So, yes, my version does work ever so slightly differently, but I feel it's
more generic. It shouldn't be the business of this function to decide which
type of file can have a `.min` slapped prior to its extension; if a caller
asks for it, let them have it, they know what they're doing! Also, although
it's not really necessary (because the code calling on it doesn't currently
pass a `Path`), it will accept either a `str` or a `Path`.

I feel the big difference here too is the testing. Rather than one method
after another, testing more or less the same thing with little variation, it
makes more sense to have just the one test and then pass it lots of
different input/output values. This is far more maintainable and also easier
to write most of the time.

Of course, for an agent, it's probably easier for it to take a copy/paste
approach than it is for it to "reason" about what makes for a maintainable
test. I sense this is one of the dangers of letting an LLM do this job (and
it's one that's often touted as being a prime job to do): good tests can be
useful documentation if you're trying to understand a codebase.
Badly-written tests, no matter how much coverage they offer, are going to
slow you down.

[//]: # (2026-05-02-me-vs-claude.md ends here)
