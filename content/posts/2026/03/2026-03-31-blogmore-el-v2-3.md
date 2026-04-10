---
title: blogmore.el v2.3
date: 2026-03-31 15:31:41+0100
category: Emacs
tags: BlogMore, Coding, Emacs, Emacs Lisp, Lisp, blogmore.el
---

I've bumped [`blogmore.el`](https://github.com/davep/blogmore.el) to v2.3.
The main change in this release, which I've had on my mental to-do list for
a couple of days now, revolves around categories, tags and case.

I've got [BlogMore](https://blogmore.davep.dev/) set up so that it's pretty
relaxed about case when it comes to categories and tags; so when it comes to
generated files and URLs everything collapses to lowercase. However,
`blogmore.el` wasn't taking this into account.

While it wasn't a serious issue, it did have the side-effect that, if you
had a tag of `lisp` and a tag of `Lisp`, both would appear in the list of
tags you could complete from. Also, when you went to add a tag to the tags
frontmatter (via the `blogmore-add-tag` command), if you selected `Lisp` and
`lisp` was already there, you'd end up with both versions after the command
finished.

> [!note]
> As mentioned earlier: BlogMore itself would collapse `Lisp` and `lisp` to
> the same tag; the downside here is you'd see both tags shown in the post
> itself. Not a real problem, just not very tidy.

So earlier I changed things up a little; first [cleaning up when loading
pre-existing values](https://github.com/davep/blogmore.el/pull/30/changes)
and then [ensuring the newly-set tags are
deduplicated](https://github.com/davep/blogmore.el/pull/31/changes).

This now means I can edit and update a post even faster, without needing to
worry about accidentally duplicating tags. This in turn reduces the friction
to writing a post for my blog. That is, after all, the whole point of the
name of the package and the blogging tool it's connected to!

[//]: # (2026-03-31-blogmore-el-v2-3.md ends here)
