---
title: blogmore.el v2.4
date: 2026-04-01 20:00:44+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, coding, blogmore.el
---

I've just released a little update to
[`blogmore.el`](https://github.com/davep/blogmore.el), adding
`blogmore-toggle-draft` as a command. This came about in connection with the
feature request that resulted in [BlogMore v2.7.0 being
released](/2026/04/01/blogmore-v2-7-0.html).

While I don't personally use `draft` for my posts, I can see the utility of
it and if someone were to happen to use `blogmore.el`, it could be useful to
have this bound to a handy key combination.

As for how it works: that's simple. When run, if there is no `draft:`
frontmatter property, then `draft: true` is added. If `draft:` is there it
is removed. Yes, it does mean that it will also remove `draft: false` too
but... eh. Okay, fine, I *might* handle that case as a followup but I
couldn't really imagine someone wanting to keep `draft: false` in the
frontmatter.

If a post is ready to go, why bother with a header that means the same thing
when it's not there?

[//]: # (2026-04-01-blogmore-el-v2-4.md ends here)
