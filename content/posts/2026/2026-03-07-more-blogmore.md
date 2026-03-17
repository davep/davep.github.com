---
layout: post
title: More BlogMore
category: Coding
tags: Python, Blogging, AI, LLM, Copilot, BlogMore
date: 2026-03-07 11:06:00 +0000
cover: attachments/2026/03/07/archive.png
---

I've just released v1.7.0 of [BlogMore](https://blogmore.davep.dev/), my
ongoing experiment with [GitHub Copilot](/tag/copilot/). Since [the last
release I wrote about](/2026/03/03/blogmore-1-5-0.html) I've made a couple
of cosmetic changes, and also addressed a couple of bugs.

The first cosmetic change relates to how the blog appears on mobile
devices[^1]. In such a circumstance, before the change, the sidebar content
would, by design, relocate to the top of the page. This made sense, it meant
that the information was still available, but it also had the unfortunate
effect of pushing the actual post content way down the screen, sometimes off
the bottom of the screen.

![The expanded view](/attachments/2026/03/07/mobile-expanded.png#centre)

Not great.

So I decided to [try and improve the mobile
layout](https://github.com/davep/blogmore/pull/202). As I have done so many
times now, I [started out with an issue that served as a
prompt](https://github.com/davep/blogmore/issues/201) and assigned it to
Copilot; despite the fairly vague request and the fact that I gave it an
image to consider, and essentially gave it a hand-waved ASCII diagram of
what I wanted, it mostly managed to one-shot the problem.

Now, when I visit the site on my phone, I see a lot less "admin" stuff at
the start.

![The collapsed view](/attachments/2026/03/07/mobile-collapsed.png#centre)

As a reader I can still toggle the "sidebar" information into view and out
of the way again, but the important thing is I can get into the post itself
right away.

Another change that's mostly cosmetic, although has a purpose too, is an
index in the archive page. I've created this to *only* be available on wider
displays; a tool to make use of any "dead" space on the right hand side of
the page. This gives a table of contents of years and months so the reader
can skip around the archives faster.

![The archive table of contents](/attachments/2026/03/07/archive.png#centre)

There have been some under-the-hood changes too. One was an effort to
[reduce the repeated boilerplate that I noticed was creeping into the
templates](https://github.com/davep/blogmore/issues/220). While I'm mainly
building this tool for myself and the "out of the box" design is how I want
my blog to look, I do want the templates to be usable and as efficient and
as easy to modify as possible.

As mentioned earlier, there's also been a couple of bug fixes; one example
being [tackling some misbehaviour on
GNU/Linux](https://github.com/davep/blogmore/issues/212) when it comes to
site generation. That issue was an interesting one in that I wasn't able to
reproduce the problem, so I decided to let Copilot have at it and make its
best deduction. From what I can tell it came through (I still need
confirmation that it has solved the problem; but it does seem to have
identified an actual edge-case that was worth taking care of).

At this point I'd also like to give a shout out to
[@andyc](https://mastodon.me.uk/@andyc). He's been a great source of testing
and feedback as I've been toying with this experiment. While I set out to
build a useful tool for me and me alone, he's raised a few good issues that
should push it in the direction of being of more general use.

I highly recommend [having a read of his post reviewing a good number of
static site
generators](https://www.yakshaving.co.uk/posts/fun-with-static-site-generators/).
As I keep tinkering with BlogMore I'll be keeping this post in mind.

[^1]: Okay fine any narrow viewport but you know what I mean!

[//]: # (2026-03-07-more-blogmore.md ends here)
