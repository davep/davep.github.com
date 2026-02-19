---
layout: post
title: A little bit of usenet
category: Tech
tags: OS X, iMac, NNTP, usenet, Homebrew
published: True
date: 2015-11-13 15:45:19+0000
---

Earlier on today I needed a copy of
[`wget`](https://www.gnu.org/software/wget/) on my iMac. It's not "native" to
it so I got to wondering how you go about getting something like that onto it.
Sure, I could have just grabbed the source and built myself, but really it's
a lot nicer to use some sort of package manager.

A quick search lead me to [Homebrew](http://brew.sh/) and I was then up and
running in no time.

This in turn got me to thinking about how it might be fun to get some of the
software I used to use on my GNU/Linux machine up and running again. The first
one that came to mind was [`slrn`](http://slrn.sourceforge.net/). Sure enough
slrn is available via Homebrew and installing it was dead simple.

But then I was faced with a problem: I needed an [NNTP](https://en.wikipedia.org/wiki/Network_News_Transfer_Protocol) server.
Way back I used to run a local one in my office that fed from and to my
ISP's. Back then my ISP was Demon Internet; these days I'm with BT. A quick
search lead me to an article or two that BT had a NNTP server, of sorts,
provided by a third party. So I did a quick check:

![Is the server there?](/attachments/2015/11/13/Screen Shot 2015-11-13 at 15.27.43.png#centre)

Yay! This looked good.

After that I fired up `slrn` and.... problems. It kept asking me to log in,
to provide a user name and password. The only problem was that I'd read in more
than one place that a user name and password weren't needed for BT's server;
all that was required was you be on a BT IP address. Checking the slrn docs
I found [`force_authentication`](http://slrn.sourceforge.net/docs/slrn-manual-6.html#ss6.32)
but ensuring that was off made no difference.

At this point I removed `slrn` and gave up.

Later, thinking it might be an issue with just `slrn` and perhaps it was worth
trying a native NNTP client, I grabbed Unison
([which is no longer supported](https://www.panic.com/blog/the-future-of-unison/)
but seems to work fine). I got that set up and ran into the same issue: it
wanted login details.

Finally, after a bit more digging, I stumbled on the reason why I was struggling
to make any of this work: [BT had closed support for the server back in
December last year](http://bt.custhelp.com/app/answers/detail/a_id/51205/?s_cid=con_FURL_giganews)!

A quick search around the web and I stumbled on [Eternal September](http://www.eternal-september.org/).
Given all I was interested in was the good old text groups this looked perfect.
I quickly registered an account, ran up Unison again and plugged in my details
and....

![Is the server there?](/attachments/2015/11/13/Screen Shot 2015-11-13 at 15.19.17.png#centre)

Now that's all sorted I should try again with `slrn`. At which point I'll need
to drag out and tidy up `post.el` ([the version that was being maintained
by some other people seems to have gone very stale](http://post-mode.sourceforge.net/), sadly).

[//]: # (2015-11-13-a-little-bit-of-usenet.md ends here)
