---
title: The webp migration is under way
date: 2026-05-06 19:45:43+0100
category: Meta
tags: Blogging, web, webp
---

I've finally made a proper start on [the planned migration to webp for
images](/2026/04/16/i-should-use-webp.html). I did consider writing a tool
that would go through and migrate the files, and update the Markdown, all in
one go, but something about that makes me kind of nervous. While it wouldn't
be a destructive approach (the whole blog [is under version control after
all](https://github.com/davep/davep.github.com)), I just have this niggling
feeling that I'd miss something and it would sit broken, unnoticed, for
ages.

So instead I've decided to take a one-post-at-a-time approach, making the
migration by hand. As well as having the benefit of letting me go slowly and
check my work as I go, I can also do some tidying up of old posts. So while
I do this I'm also going to tidy up obviously broken links when I notice
them, and also remove embedded tweets (swapping to the simple blockquote
version).

Another thing I'm doing is adding `cover` images where possible. I'd been
running this blog for a long time before I started to use `cover` (it might
be that I didn't start until [I moved to
Pelican](/2023/07/05/the-switch-has-been-made.html)). Since then I've tried
to use it any time there's an appropriate image in a post. More recently, I
[added cover images to the graph view](/2026/04/28/blogmore-v2-18-0.html) so
they're even more useful now. Back-adding a `cover` to older posts will make
them more appealing to discover in the [graph](/graph/) because those older
notes will acquire attention-grabbing thumbnails too.

One thing I wanted to do was have an easy way to keep track of where I'm up
to in the migration. It's going to be a steady process that's going to take
a few days, doing a few posts at a time. So to aid this I've added this
to the `Makefile` of the blog:

```sh
cd content/extras/attachments
find -E ./ -iregex '.*\.(png|jpg|jpeg)$' | cut -d'/' -f2,3,4 | sort -u
```

With this I get a handy list of dates of posts that still have unconverted
PNG or JPEG files.

Of course, for a wee while, this will not get to an empty list because I
want to make sure some of the more recent posts still have their older
images available as they might be in feeds out there. More recently I've
only been using `webp` for images, so once the `webp`-using posts fill the
main RSS and Atom feeds I can clean out the last of the bulkier images.

[//]: # (2026-05-06-the-webp-migration-is-under-way.md ends here)
