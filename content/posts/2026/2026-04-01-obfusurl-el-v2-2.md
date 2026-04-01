---
title: obfusurl.el v2.2
date: 2026-04-01 10:13:57+0100
category: Emacs
tags: Emacs, Emacs Lisp, Lisp, coding, obfusurl.el
---

This bit of [Emacs Lisp](/tag/emacs-lisp/) absolutely comes from a more
innocent time on the Internet. Looking at it, it seems I wrote the first
version, at least as a proper package, back in 2001. It's very possible that
I carried a non-package version of it around as part of `dp-lib.el`[^1] for
some time before, so it might date from the late 1990s. While we weren't
absolutely *innocent* back then, the idea of a slightly-risky-looking URL
wasn't quite so bad as it is now.

So `obfusurl.el` came about from my time on Usenet, where sometimes you'd
want to post a URL that would otherwise be a spoiler. This package was my
solution to that. It's a simple idea: keep the protocol and domain and so on
visible, just hide the remaining part. So rather than post:

```
https://blog.davep.org/about/
```

You'd post:

```
https://blog.davep.org/%61%62%6f%75%74/
```

I *suppose* this is still useful today, although I would expect a lot of
people to be way less likely to want to attempt that click -- readable
domain or not.

But, anyway, the code needed a tidy and cleanup for today's Emacs and Emacs
Lisp. So [`obfusurl.el` v2.2](https://github.com/davep/obfusurl.el) now
exists.

[^1]: For a good chunk of my first decade of using Emacs, I carried a lot of
    personal code around in a rather large "library" file.

[//]: # (2026-04-01-obfusurl-el-v2-2.md ends here)
