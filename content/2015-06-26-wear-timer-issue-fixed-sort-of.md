---
layout: post
title: Wear timer issue fixed, sort of
categories: []
tags: Google, Android, Wear, Android Wear, Watch, Moto360
published: True
date: 2015-06-26 12:02:31+0100
---

Following on from
[yesterday's problem with the Android Wear timer](http://127.0.0.1:4000/2015/06/25/did-google-just-break-wear-timers.html)
I think I now have a solution. It came up
[while chatting with Mike McLoughlin about the issue](https://plus.google.com/+DavePearson/posts/RZujypG7EyF).

I got to thinking that this problem felt like one that I've seen a number of
times before with Google stuff. One thing that's rather common (in many cases
for very obvious reasons -- you can't cover the whole world in one go) with
Google is how they struggle to get languages and localisation right. This
felt like it was a similar issue. Mike had reported that his watch appeared
to be unaffected by the issue (I'm guessing he's on the latest version of
Wear -- the conversation headed off in a different direction before that
became necessary) so I checked what his language was on his phone. Turns out
he was the same as me: British English.

So much for that idea.

But then he suggested switching to US English and back again.

Happy enough to apply a very Microsoft "turn it off and on again" approach to
a Google device (really, all big tech companies really are the same and
really do suffer the same issues) I switched to en-US on the phone and tried
setting a timer in voice on the watch.

It worked!

So then I switched back to en-GB on the phone and...

![I appear to have timers working again](/attachments/2015/06/26/Timer Running on Watch.png)

...it still worked!

I've tried setting timers in voice on the watch a few times since and it's yet
to fail.

It would appear, as odd as it is, that this is the fix. Well, a fix.

[//]: # (2015-06-26-wear-timer-issue-fixed-sort-of.md ends here)
