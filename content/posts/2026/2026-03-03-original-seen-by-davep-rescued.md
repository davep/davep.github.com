---
layout: post
title: Original Seen by davep rescued
category: Creative
tags: blogging, photography, BlogMore, posterous, photoblog
date: 2026-03-03 09:30:00+0000
cover: attachments/2026/03/03/still-alive.jpeg
---

![Still Alive](/attachments/2026/03/03/still-alive.jpeg#centre)

At the end of [yesterday's post](/2026/03/02/seen-by-rescued.html) I said I
might see if I can rescue the original photoblog from its [backup on
WordPress](https://seenbydavep.wordpress.com/). This was the first photoblog
I played with, posting to the long-dead
[Posterous](https://en.wikipedia.org/wiki/Posterous) between 2009 and 2013.

So, yesterday evening, I did an extract of the full feed from WordPress, and
also asked for a full backup of all the media. I then fired up Emacs and
rattled out some Python code that would marry up the two sets of data and
add to the photoblog repository. It took a little bit of working out; it
seems that every post had two entries in the feed: a parent and a child
entry. I've no clue why that's the case; I didn't really care to get too
deeply into it.

Soon enough [seen-by.davep.dev](https://seen-by.davep.dev/) was updated with
an extra 1,833 posts! So now [the
categories](https://seen-by.davep.dev/categories.html) on that blog site are
broken down into [Seen By Me
1](https://seen-by.davep.dev/category/seen-by-me-1.html) (the original) and
[Seen By Me 2](https://seen-by.davep.dev/category/seen-by-me-2.html) (the
second incarnation).

Sadly, for the first blog, tagging wasn't really much of a thing so the [tag
cloud](https://seen-by.davep.dev/tags.html) hasn't grown too much.

But, finally, I've got both the photoblogs back up and hosted somewhere I
can point to, and I'm fully in control of their content. While it is [hosted
on GitHub Pages](https://github.com/davep/seen-by) I've done this in a way
that it would be pretty easy to move elsewhere; this is down to the fact
that it's a simple static site built with
[BlogMore](https://blogmore.davep.dev/).

[//]: # (2026-03-03-original-seen-by-davep-rescued.md ends here)
