---
title: make-phony.el v1.3
date: 2026-04-03 10:23:40+0100
category: Emacs
tags: Emacs, Emacs Lisp, Lisp, coding, make-phony.el
---

A wee bit over 5 years back [I wrote a tiny package to quickly insert PHONY
target markers into a
`Makefile`](/2019/12/01/being-phony-and-lispy-regular-expressions.html).
While it's far from my most-used package, it's one that gets a call on
occasion, so it's one I still carry around in my [Emacs
configuration](https://github.com/davep/.emacs.d).

Given I'm currently engaging in a slow background process of cleaning up
some of my [Emacs Lisp](/tag/emacs-lisp/) packages, removing some [obsoleted
practices](/2022/08/23/i-must-be-getting-old.html), I've given
[`make-phony.el`](https://github.com/davep/make-phony.el) a little bit of
attention.

As well as [dropping the use of `setf` to set `point` to the start of a
line](https://github.com/davep/make-phony.el/pull/1/changes), I also tweaked
the code a little [so that it only inserts a `PHONY` if there isn't already
one there](https://github.com/davep/make-phony.el/pull/2/changes). While
that's hardly been a problem for me, it just felt like a neat bit of
cleaning up to how it works.

[//]: # (2026-04-03-make-phony-el-v1-3.md ends here)
