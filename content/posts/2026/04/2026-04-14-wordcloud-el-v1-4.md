---
title: wordcloud.el v1.4
date: 2026-04-14 08:47:39+0100
category: Emacs
tags: Emacs, Emacs Lisp, Lisp, coding, wordcloud.el
cover: /attachments/2026/04/14/wordcloud.webp
---

I *think* I'm mostly caught up with the collection of [Emacs
Lisp](/tag/emacs-lisp/) packages [that need updating and
tidying](/2022/08/23/i-must-be-getting-old.html), which means yesterday
evening's clean-up should be one of the last (although I would like to
revisit a couple and actually improve and extend them at some point).

As for what I cleaned up yesterday:
[`wordcloud.el`](https://github.com/davep/wordcloud.el). This is a package
that, when run in a buffer, will count the frequency of words in that buffer
and show the results in a fresh window, complete with the "word cloud"
differing-font-size effect.

![Word cloud in action](/attachments/2026/04/14/wordcloud.webp#centre)

This package is about 10 years old at this point, and I'm struggling to
remember *why* I wrote it now. I know I was doing something -- either
writing something or reviewing it -- and the frequency of some words was
important. I also remember this doing the job just fine and solving the
problem I needed to solve.

Since then it's just sat around in my personal library of stuff I've written
in Emacs Lisp, not really used. I imagine that's where it's going back to,
but at least it's cleaned up and should be functional for a long time to
come.

[//]: # (2026-04-14-wordcloud-el-v1-4.md ends here)
