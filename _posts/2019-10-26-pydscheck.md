---
layout: post
title: "pydscheck -- A quick hack that keeps slowly growing"
categories: []
tags: [ "python", "documentation" ]
date: 2019-10-26 13:19:00+0100
---

Something I always try to do when I'm coding is be consistent. I feel this
is important. While people's coding standards may differ, I think different
approaches are easier to handle if someone has been consistent with their
style across all of their code.

This also stands for documentation too.

In my current position, I do a *lot* of Python coding, and one of the things
I like about Python (there are things I don't like too, but that's not for
now) is that it has doc-strings (just like my [favourite
language](https://en.wikipedia.org/wiki/Common_Lisp)). I use them
extensively, ensuring every function and method has some form of
documentation, and generally I use
[Sphinx](http://www.sphinx-doc.org/en/master/) to generate documentation
from those doc-strings.

Early on I was bothered by the fact that, just by the simple act of making
typos, I wasn't keeping the form of the doc-strings consistent. And in this
case it was a *really* simple thing that was bugging me. Normally, if I'm
writing a single-line doc-string, I'll write like this:

```python
def one_liner():
    """Here is a one-line doc-string."""
```

So far, so good. But, if the doc-string is a multi-liner, I prefer the
ending quotes to be on a line of their own, like this:

```python
def multi_liner():
    """Here is the first line.
    Here is another line.
    Here is the final line.
    """"
```

But, sometimes, by accident, I'd leave a doc-string like this:

```python
def multi_liner():
    """Here is the first line.
    Here is another line.
    Here is the final line.""""
```

While it's really not a big deal, it would bug me and every time I found one
like this I'd "fix" it.

Eventually, it bugged me enough that I decided I was going to write a little
tool to find all such instances in my code and report them. My first
approach was to think "I could just do this with some regexp magic", [which
was really a bad idea](http://regex.info/blog/2006-09-15/247). Then I
though, I know, I should use this as an excuse to to play with [Python's ast
library](https://docs.python.org/3/library/ast.html).

That worked really well! I had [the first version of the
code](https://github.com/davep/pydscheck/blob/dc5052002690b1f898ccd68f815cdedbe9172b74/pydscheck)
up and running in no time. It was simple but did the job. It ran through
Python code I threw at it and alerted me to both missing doc-strings, and
doc-strings with the ending I didn't like.

That served me for a while, until one day I realised that it wasn't quite
doing the job correctly; it was only really looking at top-level functions
and top-level methods in classes. Sometimes, not often, but sometimes, I'll
define functions within functions, and I feel they deserve documentation
too. So then I modified the code to ensure it walked every part of the AST.

Since then, when I've run into new things and had new ideas, `pydscheck` has
grown and grown. I've added checks that all mentioned parameters have a
type; I've added checks that any function/method that returns something
actually documents the return value; I've added checks that any
documentation of a returned value includes its type; I've added checks that
any function or method that yields a value documents that fact; I've added
checks that ensure that every parameter is documented in some way.

Each time I've done this it's helped uncover issues in my code's
documentation that could be cleaner, and it's also given me a pet project to
slowly better understand Python's AST.

It could be that there are better tools out there, I'd have thought that a
good doc-string linting tool would be something someone had already written.
But this time around I was happy to
[NIH](https://en.wikipedia.org/wiki/Not_invented_here) it because I needed a
fun learning exercise that would also have some benefits for my day-to-day
work.

I'll caveat this with the fact that it's very particular to how I work and
how I like my documentation to look, but if it sounds useful, here it is:
[https://github.com/davep/pydscheck](https://github.com/davep/pydscheck).

There's still lots I could do with it. First off I should really properly
package it up so it can be installed as a command line tool via pip. Other
things that would be handy would be to allow some form of customisation of
how it works. I'm sure there's other fun things I can do with it too.

That's part of the fun of having a pet project: you can tinker when you like
and also get benefits from it as you use it.

[//]: # (2019-10-26-pydscheck.md ends here)
