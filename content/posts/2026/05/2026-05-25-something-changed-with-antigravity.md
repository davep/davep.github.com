---
title: Something changed with Antigravity
date: 2026-05-25 20:24:38+0100
category: AI
tags: Coding, Gemini, Google, Antigravity
cover: /attachments/2026/05/25/after-most-work.webp
---

Something has changed with [Antigravity](/tag/antigravity/) since [I first
tried it out the other day](/2026/05/20/the-gemini-bait-and-switch.html).
While looking at [adding a related posts
feature](https://github.com/davep/blogmore/issues/534) to
[BlogMore](https://blogmore.davep.dev/), I thought I'd give it another try
out (having gone back to using [Gemini CLI](/tag/gemini/) while I still
could).

That first (and last) time I tried it, while on whatever model it decided
for me out of the box, it chewed through most of the quota, with a 5 hour
reset, in very little time at all. It was obvious that I'd never get
anything of significance done in a good session.

This evening has been quite different. It wrote a [very comprehensive
change](https://github.com/davep/blogmore/pull/538), doing quite a lot of
work, and left me with a lot of quota and a short reset time once done.

![After most of the work](/attachments/2026/05/25/after-most-work.webp#centre)

A bit more testing and tweaking of the documentation followed, with me
setting it off on a couple of bug hunts (which it found and fixed). By the
time I was happy to call it an evening on this round of modifications, it had
reset and I was green across the board again.

![All done](/attachments/2026/05/25/after-done.webp#centre)

Now *this* I can work with!

I don't really know what's changed[^1], or why. I think I saw something the
other day about quotas being tripled, but this seems even more generous (at
least in terms of the reset window). I guess I'm going to have to go digging
to see if I can find what the story is.

I'm not getting my hopes up -- what can be given can be taken away at any
moment (which is, of course, the ongoing theme of what I'm documenting here)
-- but this does soften the landing somewhat.

[^1]: Although I did notice it went with `Gemini 3.5 Flash (Medium)` on
    startup and I let it go with that; last time it was `Gemini 3.5 Flash
    (High)`.

[//]: # (2026-05-25-something-changed-with-antigravity.md ends here)
