---
title: Not so elegant
category: AI
tags: AI, Coding, Copilot, LLM, Python, code review
date: 2026-03-01 11:33:00 +0000
---

One thing I've been noticing with [my current experiment with GitHub
Copilot](/2026/02/20/five-days-with-copilot.html) is that it seems to know
Python well enough to write code that gets the job done, and sometimes it
knows it well enough to write more modern idiomatic Python code, but it also
seems to write the inelegant version of it.

It's hard to pin down exactly, and of course it's a matter of taste (my idea
of elegant might burn someone else's eyes), but on occasion, as I review the
code, I find things that make me go "ugh".

Here's an example: there's a function that Copilot wrote to extract the
first non-markup paragraph of an article (so that it can be used as a page
description). One thing it needs to do is skip any initial images, etc. It
takes a pretty brute force approach of looking at the start of each stripped
line, but it gets the job done -- I can't really argue with that.

But here's how it does it:

```python
# Skip markdown image syntax
if stripped.startswith("!["):
    continue

# Skip markdown linked image syntax ([![alt](img)](url))
if stripped.startswith("[!["):
    continue

# Skip HTML img tags
if stripped.startswith("<img"):
    continue
```

Now, this is good: it's using
[`startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith).
There are less-elegant approaches it could have used so I'll give it bonus
points for using that method. The thing is though, it's testing each prefix
one string at a time, pretty much rolling out a load of boilerplate code.

What bothers me here is that `startswith` will take a tuple of strings to
test for. I find it curious that the generated code is idiomatic enough to
know that `startswith` is a sensible option here, but at the same time it
still writes the list of things to test out in a long-winded way.

This is exactly the sort of thing I'd call out in [a normal code
review](/2026/02/04/solidarity-empathy-patience.html). Technically, if this
wasn't mostly a *"let's see how it goes about this with minimal input from
me"* experiment, I'd have called it out here too (as an experiment, I might
go back prompt it to "think" about this).

If I ever find myself using this sort of tool for generating code in a work
setting, this is exactly the sort of thing I'll be watching for.

[//]: # (2026-03-01-not-so-elegant.md ends here)
