---
layout: post
title: Mandelbrot Commands
category: Python
tags: PyPi, Python, coding, Textual, mandelbrot
date: 2023-09-29 12:42:00 +0100
cover: attachments/2023/09/29/mandelbrot-commands.png
---

I don't think I've mentioned it before on this blog, but some time back I
decided it would be fun to use [Textual](https://textual.textualize.io/) to
write a Mandelbrot explorer (simple Mandelbrot explorers have been another
one of my favourite [known problem to try an unknown
thing](/2019/11/10/going-on-a-journey.html) problems). Doing it in the
terminal seemed like a fun little hack. I started off with creating
[`textual-canvas`](https://github.com/davep/textual-canvas) and then built
[`textual-mandelbrot`](https://github.com/davep/textual-mandelbrot) on top
of that.

Not too long back [I added a "command palette" to
Textual](https://textual.textualize.io/blog/2023/09/15/textual-0370-adds-a-command-palette/)
(I'd prefer to call it a minibuffer, but I get that that's not fashionable
these days), but so far I've not used it in any of my own projects; earlier
today I thought it could be fun to add it to `textual-mandelbrot`.

![Mandelbrot commands in action](/attachments/2023/09/29/mandelbrot-commands.png#centre)

Most of the commands I've added are trivial and really better covered by
(and are covered by) keystrokes, but it was a good test and a way to show
off how to create a command provider.

Having started this I can see some more useful things to add: for example it
might be interesting to add a facility where you can bookmark a specific
location, zoom level, iteration value, etc, and revisit later. The command
palette would feel like a great way to pull back those bookmarks.

What I really liked though was how *easy* this was to do. [The code to make
the commands
available](https://github.com/davep/textual-mandelbrot/blob/main/textual_mandelbrot/commands.py)
is pretty trivial and, I believe, easy to follow. Although I do say so
myself I think I managed to design a very accessible API for this.

There's more I'd like to add to that (the Textual command palette itself, I
mean), of course; this was just the start. Support for commands that accept
and prompt for arguments would be a neat and obvious enhancement (especially
if done in a way that's reminiscent of how commands could be defined in
[CLIM](https://en.wikipedia.org/wiki/Common_Lisp_Interface_Manager) -- I
remember [really liking](https://github.com/davep/org-davep-cldict/) how you
could create self-documenting and self-completing commands in that).

All in good time...

[//]: # (2023-09-29-mandelbrot-commands.md ends here)
