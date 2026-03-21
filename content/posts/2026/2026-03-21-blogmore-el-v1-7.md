---
title: blogmore.el v1.7
date: 2026-03-21 08:41:23+0000
category: Emacs
tags: Emacs, coding, Emacs Lisp, Lisp
cover: /attachments/2026/03/21/insert-link.png
---

Yes, the last time I mentioned
[`blogmore.el`](https://github.com/davep/blogmore.el) [it was
v1.4](/2026/03/20/blogmore-el-v1-4.html) and now it's up to v1.7. So I
tinkered a little with it last night, okay?

Anyway, the changes and additions keep happening as I have more fun writing
some [elisp](/tag/emacs-lisp) again. Since the last post about the package
I've:

- Added a command to refresh the `date` frontmatter property
- Added a command to add/refresh the `modified` frontmatter property
- Added a command to insert a link to a previous post into what I'm writing
- Made a few things `defcustom` rather than `defconst` for [easier
  tweaking](https://www.gnu.org/software/emacs/manual/html_node/emacs/Easy-Customization.html)
- Added a hook that can be run after a new post is started
- Dropped the dependency on [`end-it`](https://github.com/davep/end-it.el)
  and used the above hook to do the same thing

While this package is never intended for use by others, I guess it's not
impossible someone might want to work with it (I had the same thing in mind
with [BlogMore](https://blogmore.davep.dev/) itself yet someone else has
started working with it!) and so I'm moving it in the direction of being my
way by default but easy to modify to other requirements.

So, now, rather than forcing someone to have to use my obsession with
end-of-file markers, I still have that without imposing it on anyone else by
simply setting the hook.

```elisp
(use-package blogmore
  :vc (:url "https://github.com/davep/blogmore.el" :rev :newest)
  :init (add-hook 'blogmore-new-post-hook #'end-it))
```

I think my favourite addition right now is `blogmore-link-post`. I like to
cross-link posts in my blog as much as possible so having something that
lets me do that and stay inside Emacs really speeds things up. So now I just
run that command, I get speedy picker to find the post:

![Picking a post to link](/attachments/2026/03/21/insert-link.png)

and the result is some Markdown inserted with the cursor between the two
`[]` ready for me to write the text:

```markdown
[](/2026/03/20/blogmore-el-v1-4.html)
```

Other things I link often are categories and tags, so I'm planning on adding
commands that does something similar for those two.

[//]: # (2026-03-21-blogmore-el-v1-7.md ends here)
