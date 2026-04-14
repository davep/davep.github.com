---
title: Some BlogMore Elisp
category: Emacs
tags: BlogMore, Coding, Emacs, Emacs Lisp, Lisp, blogmore.el
date: 2026-03-19 15:10:28 +0000
cover: /attachments/2026/03/19/blogmore-edit.png
---

It's been a moment since I last wrote any Emacs Lisp code, at least anything
non-trivial. I've tinkered with my Emacs configuration, I've tweaked the odd
personal package here and there, but nothing fresh for ages. I actually
can't remember what the last package was that I wrote.

But this morning I realised it would be handy to have a couple of functions
in Emacs that let me start a new blog post, or edit an existing one. The
code didn't need to be clever, just the bare minimum that gets me started;
enough to reduce the friction when it comes to opening a new buffer and
starting to write.

So [blogmore.el](https://github.com/davep/blogmore.el) happened. Like I say:
nothing clever, it simply adds `blogmore-new` and `blogmore-edit`; the
former starts a new post with the bare minimum frontmatter filled in, the
latter lets me quickly pick an existing post and go edit it.

![blogmore-edit in action](/attachments/2026/03/19/blogmore-edit.png#centre)

As time goes on I might expand on this. For example: it might be useful to
have a command that updates the `date` frontmatter; perhaps another to add a
`modified`[^1]; one to set the `category` from any of the categories I've
used so far would be good; ditto the `tags` property.

I doubt this will be useful to anyone else, although I will try my best to
keep it so that it's easy to configure, so it's only ever going to stay
amongst my list of personal packages.

Which reminds me... this is the first personal package I've not bothered to
add to [delpa](https://blog.davep.org/delpa/). That approach to managing my
own packages made a ton of sense at the time, but Emacs has moved on since
then. Thanks to `use-package` and `:vc` I can easily pull `blogmore.el` into
any of my environments with a simple declaration in my
[`.emacs.d`](https://github.com/davep/.emacs.d).

```elisp
(use-package blogmore
  :vc (:url "https://github.com/davep/blogmore.el" :rev :newest))
```

Given how simple and clean that is I'm minded to "retire" delpa and use this
approach for all of my personal packages.

[^1]: Note to self: did I make [BlogMore](https://blogmore.davep.dev/)
    support modified dates?

[//]: # (2026-03-19-some-blogmore-elisp.md ends here)
