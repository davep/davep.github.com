---
title: "GitHub social preview is broken"
date: "2026-08-21 13:53:39+0100"
category: Tech
tags: [GitHub, web]
---

Earlier today, now that [Rogallo](https://rogallo.davep.dev/) has matured a
fair bit, I thought I'd update the banner image and, in doing so, refresh
the "social preview" for [the repository](https://github.com/davep/rogallo).
This is easy enough, and something I've done plenty of times with plenty of
projects. You just go into the general settings and upload a new image.

So, I faffed in Pixelmator Pro for a short while, got the new banner going,
and then uploaded it. Weirdly, it didn't preview. I was just left with a
blank rectangle.

![Borked social preview on GitHub](/attachments/2026/08/21/borked-social-preview.webp#centre)

I tried a couple more times... nothing. I then tested the repository itself
with an online "social card" checking tool and, unsurprisingly, an image was
set but it was a broken image.

Initially, I was entertaining the idea that I'd somehow done something
silly, but really it's something hard to get wrong. A little bit of
searching shows that it's not just me, with [not
one](https://github.com/orgs/community/discussions/205451) but
[two](https://github.com/orgs/community/discussions/205449) reports showing
up.

It's things like this that bother me most when using GitHub (or any other
large service). Sure, [the big outages are
bad](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/),
but with them you know they're being actively worked on, they're something
that's going to be getting constant attention until they're resolved.
Moreover, those sorts of issues generally suggest a scale problem[^1]. These
little bugs, though, suggest a lack of attention to detail, a lack of proper
testing, a lack of care about the product as a whole.

It's not even the first time in the last couple of weeks that I've run into
something like this. The other day I wanted to convert an issue into a
discussion -- a feature I've used so many times before. This time... nope.
Just didn't work. I forget exactly at what point it failed; I think the
dialog popped up and then disappeared. Whatever the now-forgotten detail of
the failure, the issue was that a long-standing, reliable feature just
stopped working.

Again: big outages can be annoying, but in those cases I tend to just go off
and do something else, either at my keyboard or, shockingly, away from it.
By the time I get back into the office it'll be sorted. These little
things... who knows when they'll be fixed?

Perhaps this bit-rot is a result of the panicked fixes to those big-bang
problems?

[^1]: Yes, of their own design. But still...

[//]: # (2026-08-21-github-social-preview-is-broken.md ends here)
