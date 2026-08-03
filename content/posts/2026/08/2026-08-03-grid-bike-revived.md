---
title: "Grid Bike revived"
date: "2026-08-03 19:59:12+0100"
category: AI
tags: [AI, Antigravity, Coding, Gemini, "Grid Bike", JavaScript, html, web]
cover: "/attachments/2026/08/03/desktop.webp"
---

If you've ever visited [my main web site](https://www.davep.org/) you might
have stumbled on [Grid Bike](https://www.davep.org/misc/grid-bike/). This
was a game that teenage me wrote on my
[VIC-20](https://en.wikipedia.org/wiki/VIC-20). I was bold enough to submit
it to Personal Computer News, and ended up having it published in the
[December 21st 1983
edition](https://archive.org/details/PersonalComputerNews/PersonalComputerNews041-21Dec1983/page/n9/mode/2up).

I still have my copy of that magazine. I've also kept a copy of scans of
that page on most versions of my website. What I haven't done, since the
early 1980s, is play the game.

I suppose, at some point, I could have grabbed a VIC-20 emulator and typed
it in. Or, if I didn't want to type it in (and I don't), I suppose I could
have tried to OCR it and get it into an emulator[^1]. But of course I never
did.

Then, a week or so back, I got to thinking: if I threw the two images at an
agent, asked it to OCR the code, and then build me a web-based version of
the game... could it manage it?

So, on a whim, yesterday evening, sat on a bed in a hotel [in
Whitby](/2026/08/02/fossil-hunting-in-whitby.html), I threw a prompt at
[Antigravity](/tag/antigravity/):

> In this directory you will find grid-bike-page-1.jpg and
> grid-bike-page-2.jpg -- these are two scans from a magazine from the early
> 1980s, that contain a game I wrote for the VIC-20. I want you to OCR the
> images to pull out the code, understand the code, and then create a
> faithful recreation of the game as a standalone webpage, with the game
> written in JavaScript, so that I can play the game once again.

Initially it wanted to install `PIL` globally and kick off the work that
way; I wasn't allowing that so I had to tell it to use `uv` instead and make
a virtual environment in which to work. After that it didn't take too long
to OCR the code, comprehend it, and write the website. The first version
ended up looking far better than I was expecting.

What followed was about an hour of refinement as I got it to fix some visual
problems (the characters it used for the lines didn't quite line up on the
corners, for example), some audio problems (trying to get it to recreate the
sound of the bike I had going on the VIC proved tricky, and it's still not
how I remember it), and also a handful of playability issues when it came to
mobile devices.

![The desktop version](/attachments/2026/08/03/desktop.webp#centre)

Eventually though it got to a point where, without question, I had a version
of the original game, as I played it on my VIC, running in my browser --
both on desktop and on my iPhone.

![The mobile version](/attachments/2026/08/03/mobile.webp#centre)

I suspect it still needs some more refinement. The placement and layout of
the opening text isn't quite right, I don't think, and the audio could still
be better. Also, I'm finding the sound toggle button doesn't quite work as I
think it should (depending on when you turn it off, it seems like it might
or might not actually turn off the sound). I'm also not convinced the
"Keyboard Controls" panel is as readable as it could be.

Without question though, it's playable and it's my original game, brought
back off the page.

If you fancy having a muck about yourself, it's at
[grid-bike.davep.dev](https://grid-bike.davep.dev).

[^1]: And given how well this has gone, I might try that.

[//]: # (2026-08-03-grid-bike-revived.md ends here)
