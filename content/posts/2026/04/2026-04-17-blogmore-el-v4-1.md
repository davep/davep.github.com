---
title: blogmore.el v4.1
date: 2026-04-17 10:25:37+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, blogmore.el, coding, web, webp
---

Following on from [yesterday's experiment with
webp](/2026/04/16/i-should-use-webp.html) I got to thinking that it might be
handy to add a wee command to
[`blogmore.el`](https://github.com/davep/blogmore.el) that can quickly swap
an image's extension from whatever it is to `webp`.

So [v4.1](https://github.com/davep/blogmore.el/releases/tag/v4.1) has
happened. The new command is simple enough, called
`blogmore-webpify-image-at-point`; it just looks to see if there's a
Markdown image on the current line and, if there is, replaces the file's
extension with `webp` no matter what it was before.

If/when I decide to convert all the `png` files in the blog to `webp` I'll
obviously use something very batch-oriented, but for now I'm still
experimenting, so going back and quickly changing the odd image here and
there is a nicely cautious approach.

I have, of course, added the command to the transient menu that is brought
up by the `blogmore` command.

One other small change in v4.1 is that a newly created post is saved right
away. This doesn't make a huge difference, but it does mean I start out with
a saved post that will be seen by [BlogMore](https://blogmore.davep.dev/)
when generating the site.

[//]: # (2026-04-17-blogmore-el-v4-1.md ends here)
