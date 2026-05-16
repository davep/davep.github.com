---
title: Gemini CLI vs GitHub Copilot (redux)
date: 2026-05-16 09:30:23+0100
category: AI
tags: BlogMore, Coding, Copilot, Gemini, GitHub, Google, Python
---

Given I'm [almost certainly](/2026/05/13/the-copilot-bait-and-switch.html)
going to drop GitHub Copilot starting next month, I'm using Gemini CLI more
and more for [BlogMore](https://blogmore.davep.dev/). Yesterday evening, I
used it to plan out an idea for a change to the application. Now that I've
[migrated all images to WebP](/2026/05/15/converted-to-webp.html), I thought
it might be interesting to look at the idea of having a responsive approach
to images. This is something I don't know a whole lot about (never having
needed to bother with it before), but it also happens that I need to read up
on this anyway for something related to the day job; given this, it felt
like a good time to experiment.

Together with Gemini CLI [a plan was
created](https://github.com/davep/blogmore/issues/490).

This morning, over second coffee, I've kicked off the job of implementing it
and, honestly, Gemini CLI is really struggling. It "implemented" the change
pretty quickly, within minutes, but it just plain didn't work. Since then
I've had it iterate over the issue four times and now it's struggling to
make it work at all. It's still beavering away on this as I type, and
consuming daily quota at a fair rate too.

So, while I still have GitHub Copilot, this feels like a good point to play
them off against each other at least one more time. Having saved the plan
Gemini wrote last night as an issue, [I've assigned it to
Copilot](https://github.com/davep/blogmore/pull/491) (using Claude Sonnet
4.6). As I type this, I have Gemini racing to get this working in a terminal
window behind Emacs, meanwhile there's Claude doing its thing in GitHub's
cloud.

It'll be interesting to see if Copilot manages to one-shot this, for sure
Gemini is far off a one-shot implementation.

[//]: # (2026-05-16-gemini-cli-vs-github-copilot-redux.md ends here)
