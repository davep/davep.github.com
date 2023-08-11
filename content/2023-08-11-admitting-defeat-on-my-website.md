---
layout: post
title: Admitting defeat on my website
category: Coding
tags: php, html, web
date: 2023-08-11 08:44:00 +0100
---

I've had `davep.org` since very late 1999. Initially it started as a domain
used just for email; while I did have a website, around that time it was
still hosted on my then-ISPs hosting service, with a mirror on a friend's
web server.

A year or so later I finally did a proper revamp of my website and finally
settled on `www.davep.org` as the place to point people to. I *think*, when
I made that move, that's when I decided to write my own website engine in
php. It was fun. It worked. I didn't want to code backend stuff (I don't
think the backend vs frontend distinction was even a thing we were talking
about then) so hacking it together in an unholy mix of ruby to generate
various static files that live in the filesystem and then php to turn them
into actual HTML made sense.

And it worked.

![The earliest version of davep.org I can find](/attachments/2023/08/11/davep-org.png#centre)

I heavily maintained the site for many years; keeping the same engine,
tweaking the styles, adding features and content. I figure some time around
2013 or 2014 I probably stopped being quite so active in messing with it,
and then in the last 5 or 6 years I've pretty much neglected it.

The neglect shows.

Meanwhile... php has changed. Quiet a lot. It's one of those languages I
used back in the day and pay no attention to. Then earlier this week I
noticed that there must have been an update on the host and huge parts of my
site broke, lots of content missing, pretty much useless and dead in the
water.

I did briefly think about breaking out the latest and greatest php locally,
setting things up to investigate what's going on, and seeing if I could
breathe some more life into it; but really what's the point?

So after all these years I'm finally admitting defeat.

Right now, on the home page, I've just got a placeholder saying that bitrot
finally ate my website and that I'm going to start again from scratch.
That's my plan: given that [I had a good experience moving this blog over to
Pelican](https://blog.davep.org/2023/07/05/the-switch-has-been-made.html) I
think I'm going to build a new `www.davep.org` with Pelican. Where possible
I'll try and drag some of the old content over, but I'm also going to use
this opportunity to have a proper digital spring clean.

There's no planned timescale for this, but this morning I've spent an hour
or so over coffee, branching the repo for the site and pruning out all the
stuff I know I won't need and don't want.

I'll try and drop the odd update in here as things progress.

[//]: # (2023-08-11-admitting-defeat-on-my-website.md ends here)
