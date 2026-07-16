---
title: "gemtext - A Gemtext parsing library for Python"
date: "2026-06-25 12:05:42+0100"
category: Python
tags: [Coding, "Gemini Protocol", PyPI, Python, gemtext, smolweb]
---

I've just made an initial release of a new library related to my [ongoing
project to build my own Gemini protocol browser](/tag/rogallo/). Initially,
the code to parse the [hypertext
format](https://geminiprotocol.net/docs/gemtext-specification.gmi) used for
Gemini sites, lived in the Rogallo codebase. But despite it being a pretty
simple bit of code, I felt it could be useful for other things too. So
rather than have it be buried inside a package that has a lot of other
dependencies, I've decided to spin it out into its own little package.

So [`gemtext`](https://gemtext.davep.dev/) v0.1.0 is [now
available](https://pypi.org/project/gemtext/). The library provides a single
parsing class, which takes raw markup as a string and turns it into a
sequence of objects, each typed for the type of line found. A very simple
parsing tool might look like this:

```python
import fileinput
from gemtext import Gemtext

def parse_input() -> None:
    for gem_line in Gemtext("".join(fileinput.input())).content:
        print(f"{gem_line!r}")
```

If fed with the following input:

````gemtext
# This is a heading

## This is a sub-heading

### This is a sub-sub-heading

=> gemini://davep.gemcities.com/ Dave's test capsule

> This is a deep and meaningful quote

```
Here is some pre-formatted text.

Here's some more of that text.
```

* One
* Two
* Three
````

the output would be this:

```python
Heading(content='This is a heading', level=1)
Paragraph(content='')
Heading(content='This is a sub-heading', level=2)
Paragraph(content='')
Heading(content='This is a sub-sub-heading', level=3)
Paragraph(content='')
Link(content="Dave's test capsule", uri='gemini://davep.gemcities.com/')
Paragraph(content='')
Quote(content='This is a deep and meaningful quote')
Paragraph(content='')
PreFormatted(content="Here is some pre-formatted text.\n\nHere's some more of that text.")
Paragraph(content='')
ListItem(content='One')
ListItem(content='Two')
ListItem(content='Three')
```

That's the extent of the library for the moment. I don't see it growing too
much, given how straightforward the markup language is. Perhaps one addition
I might make at some point is a method of going the other way: allow
collecting together each of the [individual line-oriented
objects](https://gemtext.davep.dev/gemtext/) and getting a text document
back, so providing an object-oriented interface for producing Gemtext
documents.

For now though this is enough to support what Rogallo needs.

[//]: # (2026-06-25-gemtext-a-gemtext-parsing-library-for-python.md ends here)
