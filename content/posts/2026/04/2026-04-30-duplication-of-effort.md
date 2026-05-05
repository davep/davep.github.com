---
title: Duplication of effort
date: 2026-04-30 08:20:11+0100
category: AI
tags: BlogMore, Coding, Copilot, Gemini, GitHub, Google, Python, code review, code smell
cover: /attachments/2026/04/30/review-diff.webp
---

While I don't, for a moment, think that the work on
[BlogMore](https://blogmore.davep.dev/) is complete, I think it's fair to
say that the rate of new feature additions has slowed down. Which is fine,
there's only so much I need from a self-designed/directed static site
generator; at a certain point there's a danger of [adding features for the
sake of it](/graph/).

Around this point I think I want to start to pay proper attention to the
code quality and maintainability [of the ongoing
experiment](/2026/02/20/five-days-with-copilot.html).

As [I mentioned the other day](/2026/04/26/but-is-the-code-that-bad.html),
while working through this, I had noticed plenty of bad habits that Copilot
(and in this case pretty much always Claude Sonnet 4.6) has. All were very
human (obviously), but also the sort of thing you'd expect a human developer
to educate themselves out of.

Yesterday evening, out of idle curiosity, I installed [Gemini
CLI](https://geminicli.com/) because I wanted to see what would happen if I
pointed it at the [v2.18.0
codebase](https://github.com/davep/blogmore/tree/v2.18.0) and asked it to
look for things to clean up, and then what would happen if I did the same
with [Copilot CLI](https://github.com/features/copilot/cli).

I've saved the results as [a PR for what Gemini came up
with](https://github.com/davep/blogmore/pull/426) and [what Copilot came up
with](https://github.com/davep/blogmore/pull/427)[^1]. I've not given them a
proper read over yet, but while having a quick glance at them something
leapt out at me: in the code before the request, there was this in
`utils.py`:

```python
def count_words(content: str) -> int:
    """Count the number of words in the given content.

    Strips common Markdown and HTML formatting before counting so that only
    prose words are included.  The same normalisation rules as
    :func:`calculate_reading_time` are applied.

    Args:
        content: The text content to analyse (may include Markdown/HTML).

    Returns:
        The number of words in the content.

    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("word " * 10)
        10
    """
    # Remove code blocks
    content = re.sub(r"```[\s\S]*?```", "", content)
    content = re.sub(r"`[^`]+`", "", content)

    # Remove markdown links but keep the text: [text](url) -> text
    content = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", content)

    # Remove markdown images: ![alt](url) -> ""
    content = re.sub(r"!\[([^\]]*)\]\([^\)]+\)", "", content)

    # Remove HTML tags
    content = re.sub(r"<[^>]+>", "", content)

    # Remove markdown formatting characters
    content = re.sub(r"[*_~`#-]", " ", content)

    return len([word for word in content.split() if word])


def calculate_reading_time(content: str, words_per_minute: int = 200) -> int:
    """Calculate the estimated reading time for content in whole minutes.

    Uses the standard reading speed of 200 words per minute. Strips markdown
    formatting and counts only actual words to provide an accurate estimate.

    Args:
        content: The text content to analyze (can include markdown)
        words_per_minute: Average reading speed (default: 200 WPM)

    Returns:
        Estimated reading time in whole minutes (minimum 1 minute)

    Examples:
        >>> calculate_reading_time("Hello world")
        1
        >>> calculate_reading_time("word " * 400)
        2
    """
    # Remove code blocks (they typically take longer to read/understand)
    content = re.sub(r"```[\s\S]*?```", "", content)
    content = re.sub(r"`[^`]+`", "", content)

    # Remove markdown links but keep the text: [text](url) -> text
    content = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", content)

    # Remove markdown images: ![alt](url) -> ""
    content = re.sub(r"!\[([^\]]*)\]\([^\)]+\)", "", content)

    # Remove HTML tags
    content = re.sub(r"<[^>]+>", "", content)

    # Remove markdown formatting characters
    content = re.sub(r"[*_~`#-]", " ", content)

    # Count words (split by whitespace and filter out empty strings)
    words = [word for word in content.split() if word]
    word_count = len(words)

    # Calculate minutes, rounding to the nearest minute with a minimum of 1
    minutes = max(1, round(word_count / words_per_minute))

    return minutes
```

I think this right here is a great example of why the code that these tools
produce is generally kind of... meh. Let's just really appreciate for a
moment the duplication of effort going on there. But it's even more fun.
Look at the docstring[^2] for `count_words`: it says right there that the
*"same normalisation rules as `calculate_reading_time` are applied"*. It
"knows" it copied the work that went into `calculate_reading_time` too, but
never once did it then "think" to pull the common code out and have both of
the functions call on that helper function.

Back to the parallel invitations to refactor, having asked:

> please do a review of this codebase and see if there is any scope for
> refactoring so there's less duplication

Both Gemini *and* Claude noticed this and did something about it. Gemini
came up with a:

```python
def _strip_formatting(content: str) -> str:
```

with all the regex-based-markdown-stripping code in there and then rewrote
`count_words` and `calculate_reading_time` to call on that. The
Copilot/Claude cleanup did something very similar:

```python
def _strip_markdown_formatting(content: str) -> str:
```

So it's a good thing that both of them "noticed" this duplication of effort
and cleaned it up. What I *do* find interesting though is what the result
was. Stripping docstrings and comments for a moment, here's what I was left with, by
Gemini, for `count_words` and `calculate_reading_time`:

```python
def count_words(content: str) -> int:
    content = _strip_formatting(content)
    return len([word for word in content.split() if word])

def calculate_reading_time(content: str, words_per_minute: int = 200) -> int:
    content = _strip_formatting(content)
    words = [word for word in content.split() if word]
    word_count = len(words)
    minutes = max(1, round(word_count / words_per_minute))
    return minutes
```

and here's what Copilot/Claude came up with:

```python
def count_words(content: str) -> int:
    return len([word for word in _strip_markdown_formatting(content).split() if word])

def calculate_reading_time(content: str, words_per_minute: int = 200) -> int:
    words = [word for word in _strip_markdown_formatting(content).split() if word]
    return max(1, round(len(words) / words_per_minute))
```

In both cases `calculate_reading_time` is still doing the work of counting
words when `count_words` is right there to be called! Don't even get me
started on how the Gemini version of `calculate_reading_time` is so obsessed
with assigning values to variables that only get used once in the next
line[^3]. Were I reviewing these PRs (oh, wait, I *am* reviewing these
PRs!), I'd request the latter function be turned into:

```python
def calculate_reading_time(content: str, words_per_minute: int = 200) -> int:
    return max(1, round(count_words(content) / words_per_minute))
```

I would imagine that there's a lot more of this going on in the code, and
under ideal conditions this sort of thing would *not* have made its way into
the codebase in the first place. Part of the point of this experiment was to
mostly get the agent to do its own thing, without me doing full-on reviews
of every PR. Were I to use this sort of tool in a workplace, or even on a
FOSS project that wasn't intended to be this exact experiment, I'd be far
more inclined to carefully review the result and request changes.

Or, perhaps, hear me out... I have a third agent that I teach to be just
like me and I get *it* do the work of reviewing the PRs for me. What could
possibly go wrong?

[^1]: Again, I guess I should stop referring to Copilot in this case and
    instead refer to Claude Sonnet.
[^2]: Note to self: I need to educate the agents in how I prefer and always
    use the mkdocstrings [style of
    cross-references](https://mkdocstrings.github.io/usage/?h=reference#cross-references).
[^3]: Yes, I know, this is a favoured clean code kind of thing in some
    circles, but it can be taken to an unnecessary extreme.

[//]: # (2026-04-30-duplication-of-effort.md ends here)
