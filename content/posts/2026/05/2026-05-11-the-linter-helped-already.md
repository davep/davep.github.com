---
title: The linter helped already
date: 2026-05-11 08:29:57+0100
category: Meta
tags: BlogMore, Blogging, web, webp
---

The new linting tool I've [added to
BlogMore](/2026/05/10/blogmore-v2-21-0.html) has paid off already. While it
is the case that it helped me find a couple of broken links and one or two
other things to tidy, as I was working on the feature; by the time I
released it, my blog was lint-free.

But last night I did a little more work on [the slow migration of images
over to WebP](/2026/05/06/the-webp-migration-is-under-way.html). As I've
mentioned before: this is a process I'm doing by hand, one post at a time,
for a couple of different reasons. The thing is, I'm in a part of my blog
now where I was often posting about updates to projects I was working on
([Tinboard](/tag/tinboard/) being a good example), and the `cover` for all
of the posts would be the same. To save having multiple copies of the cover
image, all subsequent posts would point back to the first cover image[^1].

So what was happening was, I'd have a cover image that got transitioned from
PNG to WebP, and then the covers of a number of posts, later in time, would
be broken. While I would get to them eventually, if I'd called it a day
there and rebuilt my blog, those would have been published broken.

Using `blogmore lint` while making those changes yesterday evening alerted
me to this right away.

[^1]: It's worth noting that I break down the post attachments [by
    day](https://github.com/davep/davep.github.com/tree/main/content/extras/attachments).

[//]: # (2026-05-11-the-linter-helped-already.md ends here)
