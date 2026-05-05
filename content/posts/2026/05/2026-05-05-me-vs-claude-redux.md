---
title: Me vs Claude (redux)
date: 2026-05-05 20:30:24+0100
category: AI
tags: BlogMore, Coding, Copilot, GitHub, Python, code review, code smell
---

It's a small thing, but here's round 2 of [me vs
Claude](/2026/05/02/me-vs-claude.html). This time I'm directing the agent to
clean up the code that does word counts, getting it to use the Markdown to
plain text code that exists in [BlogMore](/tag/blogmore/), rather than the
regex-based Markdown-stripper it was using. The approach it landed on made
sense to me, adding another text extractor class, but one that ignores
fenced codeblocks[^1]. So, in addition to this code (I've removed all
docstrings and comments for the sake of including here):

```python
class _AllTextExtractor(HTMLParser):

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        self._chunks.append(data)

    @property
    def text(self) -> str:
        return re.sub(r"\s+", " ", "".join(self._chunks)).strip()
```

it also added this:

```python
class _TextWithoutCodeExtractor(HTMLParser):

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []
        self._pre_depth: int = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "pre":
            self._pre_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self._pre_depth > 0:
            self._pre_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._pre_depth == 0:
            self._chunks.append(data)

    @property
    def text(self) -> str:
        return re.sub(r"\s+", " ", "".join(self._chunks)).strip()
```

The function that converts Markdown to plain text then decides which
extractor to use, based on if the caller asked for codeblocks to be included
or not.

All pretty reasonable.

Only... that `text` property on both those classes is identical. The
`__init__` method is the same save for one extra line. Even `handle_data` is
more or less the same except for that guarding `if`.

I can't. I can't let that stand. It's almost copy/paste. For me, this is the
ideal time to use just a little bit of inheritance. Here's my take (with
classes renamed too, the leading `_` didn't feel necessary for one thing):

```python
class TextExtractor(HTMLParser):

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._chunks: list[str] = []

    def handle_data(self, data: str) -> None:
        self._chunks.append(data)

    @property
    def text(self) -> str:
        return re.sub(r"\s+", " ", "".join(self._chunks)).strip()


class TextSansCodeExtractor(TextExtractor):

    def __init__(self) -> None:
        super().__init__()
        self._pre_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "pre":
            self._pre_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "pre" and self._pre_depth > 0:
            self._pre_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._pre_depth == 0:
            super().handle_data(data)
```

Much better!

I was tempted to prompt Copilot/Claude about this and see what clean-up it
would do, if it would arrive at similar code. But really it didn't seem like
a good use of a premium request (perhaps I should have given Gemini a shot).

I see this kind of thing in the code quite a bit, and it speaks to what I've
said before about what I'm seeing: the code it writes is... fine. It's okay.
It does the job. The code runs. It's just not... to my taste, I guess.

[^1]: This is important for working out word counts and so read times. It
    doesn't make sense that embedded code counts towards those.

[//]: # (2026-05-05-me-vs-claude-redux.md ends here)
