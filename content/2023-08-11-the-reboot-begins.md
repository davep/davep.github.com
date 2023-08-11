---
layout: post
title: The reboot begins
category: Coding
tags: html, web
date: 2023-08-11 13:19:00 +0100
---

And I'm off! This morning I spent a good amount of time going through the
sources for the old version of [`davep.org`](http://www.davep.org) and
removing everything that won't be needed any more, and also building up a
rough TODO list of things I may want to recreate as content.

With that done, [as mentioned earlier
today](/2023/08/11/admitting-defeat-on-my-website.html), I started work on
building the site around Pelican. Pretty quickly though I started to feel
that that was going to be a bad choice. While Pelican felt like a *perfect*
fit for this blog -- mainly because it seems to be very blog-oriented -- it
was feeling a bit clunky for a general website that would have a handful of
static pages at best; likely something I wouldn't be updating too often.

So I put it aside and went on with my morning, doing normal Friday domestic
stuff like the weekly supermarket shop. It was while I was out doing that
that I realised the obvious answer: use [what we use for the Textual
docs](https://textual.textualize.io/) and what's been used for
[`label.dev`](https://label.dev/): [Material for
MkDocs](https://squidfunk.github.io/mkdocs-material/)!

I've just spent about 40 minutes after lunch kicking that off and it was
really straightforward. Of course the result is horrifically cookie-cutter
in terms of its look -- such is the way that `mkdocs-material` sites end up
looking out of the box -- but I don't much care about that; what's important
is that I've got a placeholder page in place, and I've quickly built a
framework for writing and publishing the content.

So that's the plan: now that the welcome page is in place and there's
*something* on my domain that looks like a working website again I can start
to slowly drag in old content in a new format. Heck, if I'm careful I might
even be able to retain some of the old URLs!

Longer-term plans might involve finally sorting out `https` support (yes,
even today, my site is `http`-only), and perhaps adding some sort of RSS
feed so there's a record of when changes are made.

After that... hopefully that'll be about it and perhaps the website will
last another 22 years running on top of the same engine (actually that part
should be easier because the "engine" is now local and it generates a static
site).

The question then becomes who'll last longer, the site or me?

[//]: # (2023-08-11-the-reboot-begins.md ends here)
