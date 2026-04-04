---
title: blogmore.el v2.0
date: 2026-03-29 20:50:41+0100
category: Emacs
tags: BlogMore, Coding, Emacs, Emacs Lisp, Lisp, blogmore.el
cover: /attachments/2026/03/29/customize-blogmore.png
---

After [kicking off `blogmore.el`](/2026/03/19/some-blogmore-elisp.html), and
then tinkering with it [more](/2026/03/20/blogmore-el-v1-4.html) and
[more](/2026/03/21/blogmore-el-v1-7.html), I've found it really quite
helpful while writing posts. One thing I have noticed though -- given I use
[BlogMore](https://blogmore.davep.dev/) for this blog and [my
photoblog](https://seen-by.davep.dev/) -- is that I wanted to be able to use
the package for working with more than one blog.

So today I found myself with some time to kill and the result is that
`blogmore.el` v2.0 has now been released. This version allows for setting up
multiple blogs, each with their own settings for where posts live, how their
paths are formatted, and so on.

To handle this I've also added the `blogmore-work-on` command so that the
active blog can be quickly changed.

All of this can be configured using Emacs' customize feature.

![Customize blogmore](/attachments/2026/03/29/customize-blogmore.png#centre)

This has all changed since v1.x, where most of the customize options have
now been renamed to include `-default-` in their name. The idea here is that
what was *the* value for a setting previously is now the default value if a
given blog hasn't had that setting defined.

For any given blog you wish to work with, you configure a name (for your own
reference) and the path to the posts. Optionally you can also set lots of
other values too.

![Customize the blog](/attachments/2026/03/29/customize-blogs.png#centre)

If a value is left on `Default`, then the corresponding default setting will
be used; if it's set, then that value is used for that specific blog.

The defaults out of the box match how I do things with my blogs, of course,
so the configuration is pretty straightforward. As of the time of writing my
[`use-package`](https://www.gnu.org/software/emacs/manual/html_node/use-package/)
for `blogmore.el` looks like this:

```elisp
(use-package blogmore
  :vc (:url "https://github.com/davep/blogmore.el" :rev :newest)
  :init (add-hook 'blogmore-new-post-hook #'end-it)
  :custom
  (blogmore-blogs
   '(("blog.davep.org" "~/write/davep.github.com/content/posts/")
     ("seen-by.davep.dev" "~/write/seen-by/content/posts/")))
  :bind
  ("<f12> m b" . blogmore-work-on)
  ("<f12> m p n" . blogmore-new)
  ("<f12> m p e" . blogmore-edit)
  ("<f12> m s c" . blogmore-set-category)
  ("<f12> m a t" . blogmore-add-tag)
  ("<f12> m u d" . blogmore-update-date)
  ("<f12> m u m" . blogmore-update-modified)
  ("<f12> m l p" . blogmore-link-post)
  ("<f12> m l c" . blogmore-link-category)
  ("<f12> m l t" . blogmore-link-tag))
```

In the above you can see that I've set only the blog title and posts path
for each blog in `blogmore-blogs`; the remaining values are all implied
`nil` and so will be defaulted. The full list of values for any given blog
are:

```elisp
(BLOG-NAME
 POSTS-DIRECTORY
 POST-TEMPLATE
 POST-MAKER-FUNCTION
 CATEGORY-MAKER-FUNCTION
 TAG-MAKER-FUNCTION
 POST-LINK-FORMAT
 CATEGORY-LINK-FORMAT
 TAG-LINK-FORMAT)
```

where:

- `BLOG-NAME` is the descriptive name to use for the blog.
- `POSTS-DIRECTORY` is the directory where the blog's posts are stored.
- `POST-TEMPLATE` is a template for new posts. If `nil`,
  `blogmore-default-template` is used.
- `POST-MAKER-FUNCTION` is a function that takes a filename and returns a
  string to be used in the post's URL. If `nil`,
  `blogmore-default-post-maker-function` is used.
- `CATEGORY-MAKER-FUNCTION` is a function that takes a category name and
  returns a string to be used in the category's URL. If `nil`,
  `blogmore-default-category-maker-function` is used.
- `TAG-MAKER-FUNCTION` is a function that takes a tag name and returns a
  string to be used in the tag's URL. If `nil`,
  `blogmore-default-tag-maker-function` is used.
- `POST-LINK-FORMAT` is a format string for the post's URL, where `%s` is
  replaced with the value returned by the post maker function. If `nil`,
  `blogmore-default-post-link-format` is used.
- `CATEGORY-LINK-FORMAT` is a format string for the category's URL, where
  `%s` is replaced with the value returned by the category maker function. If
  `nil`, `blogmore-default-category-link-format` is used.
- `TAG-LINK-FORMAT` is a format string for the tag's URL, where `%s` is
  replaced with the value returned by the tag maker function. If `nil`,
  `blogmore-default-tag-link-format` is used.

While I very much doubt any of this is useful to anyone else, it's at least
flexible for my purposes and can probably be configured to someone else's
purpose should they happen to be using BlogMore and Emacs.

[//]: # (2026-03-29-blogmore-el-v2-0.md ends here)
