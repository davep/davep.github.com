---
title: blogmore.el v1.4
category: Emacs
tags: Emacs, Emacs Lisp, Lisp, blogmore.el, coding
date: 2026-03-20 08:46:59 +0000
cover: /attachments/2026/03/20/string-split.png
---

Following on from [yesterday's post](/2026/03/19/some-blogmore-elisp.html),
in the evening I found myself in a cafe with my MacBook Pro and an hour to
kill, so I tinkered with [blogmore.el](https://github.com/davep/blogmore.el)
a little more. The main aim here was to add a command for adding tags to a
post and I now have `blogmore-add-tag` as of v1.4.

One thing that stood out was just how rusty my Emacs Lisp skills are. It
took me a wee while to get the code working, mostly due to me being caught
out by the gotchas I'd forgotten about surrounding match data and the need
to make good use of
[`save-match-data`](https://www.gnu.org/software/emacs/manual/html_node/elisp/Saving-Match-Data.html)
(I had a combination of `re-search-forward`, `string-split` and
`replace-match` going on and it was chaos for a while).

I got there in the end, though, when I bothered to RTFM with a quick `C-h f
string-split RET`.

![Documentation for string-split](/attachments/2026/03/20/string-split.png#centre)

So now I have the following commands in Emacs when I get the urge to do
something blog-related:

- `blogmore-new` starts a new blog post
- `blogmore-edit` lets me edit an existing post
- `blogmore-set-category` lets me set the category from existing categories,
  or set a new one
- `blogmore-add-tag` lets me add a tag from the existing tags, or add a new
  one

As suggested before, I think I'll probably add some other helper commands,
things such as:

- Update the `date`
- Set the `cover` to a particular attachment
- Insert a particular attachment as a Markdown image
- Insert a link to another post in the blog

I'm sure more will come to me, but they seem like the most common operations
I perform that would be helped with a little bit of Emacs Lisp magic.

[//]: # (2026-03-20-blogmore-el-v1-4.md ends here)
