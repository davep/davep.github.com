---
title: blogmore.el v2.1
date: 2026-03-30 16:20:22+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, coding, Unix
---

I've given [`blogmore.el`](https://github.com/davep/blogmore.el) a wee bump
to v2.1. This release fixes a small problem I noticed today when I tried to
use it to edit the tags for [a post on my
photoblog](https://seen-by.davep.dev/2026/03/30/refactored.html): the code
to find and gather properties from posts didn't handle deeply-nested
directory hierarchies for the post markdown files. I should have noticed
this when I first wrote the code, but of course I was so busy testing
against my primary blog, which only goes one sub-level deep, that I never
noticed it wasn't going to work deeper.

So rather than using `grep` to look for things like `foo/**/*.md` I swapped
to a combination of `find` and `grep`. Which works, but is slightly (but
noticeably) slower.

Then I got to thinking that if I was doing this by hand, on the command
line, I'd be using [ripgrep](https://github.com/burntsushi/ripgrep) anyway.
Given this I might as well use it here. Of course, not everyone who might
use `blogmore.el` will have `rg` installed so it makes sense to look for
that and use it if it's available, otherwise fall back on `find`/`grep`.

There's still some low-priority cleaning up I want to do around this; an
obvious change I want to make being one where I want to collapse all cases
of the same word (Tree vs tree, etc) into one "hit"[^1]. For now though, as
always, it's working well enough for *my* needs and this change fixed an
obvious issue I ran into.

[^1]: [BlogMore](https://blogmore.davep.dev/) itself takes care of this, but
    it would be nice to have the prompt in `blogmore.el` also take this into
    account.

[//]: # (2026-03-30-blogmore-el-v2-1.md ends here)
