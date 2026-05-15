---
title: Converted to WebP
date: 2026-05-15 19:27:00+0100
category: Meta
tags: Blogging, web, webp
---

The job is finally done. After [considering moving all the images in the
blog over to WebP](/2026/04/16/i-should-use-webp.html), and then [finally
getting the migration under
way](/2026/05/06/the-webp-migration-is-under-way.html), I'm all done.

As I mentioned before: I've done this by hand, one post at a time, also
adding missing `cover`s as I go. The process went faster than I anticipated
and I found that [adding linting support to
BlogMore](/2026/05/10/blogmore-v2-21-0.html) really helped with this
process. Each time I made a batch of changes I could run the linter to make
sure I'd not broken any image links.

As for the result: I've brought the total size of images on the blog down
from around 56MB to about 32MB, give or take (keep in mind the latter figure
also includes all the WebP images I've added while blogging since I started
this process). While I don't really have to worry so much about the storage
costs of these images ([I'm
using](https://github.com/davep/davep.github.com) GitHub Pages after all),
overall, over time, there should be savings in the time it takes for readers
to load any given page.

[//]: # (2026-05-15-converted-to-webp.md ends here)
