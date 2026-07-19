---
title: "Some documentation in Geminispace"
date: "2026-07-19 20:50:55+0100"
category: Tech
tags: [Blogging, Coding, "Gemini Protocol", Markdown, gemtext, smolweb]
---

Given that [Rogallo](/tag/rogallo/) is coming on pretty well, I feel it's
about time to get some sort of documentation for it going *in* Geminispace.
With this in mind, I've created an account over on
[tilde.team](https://tilde.team/) so I can make use of [their support for
the Gemini protocol](https://tilde.team/wiki/gemini).

While I don't imagine I'll be writing documentation as comprehensive as [the
main site for Rogallo](https://rogallo.davep.dev/), I do aim to provide
[some basic information](gemini://tilde.team/~davep/rogallo/).

The other thing I'm going to maintain there is [a version of the change
log](gemini://tilde.team/~davep/rogallo/changelog.gmi). Rather than edit it
by hand each time, I've [added a tool to the Rogallo
repository](https://github.com/davep/rogallo/blob/main/docs/bin/log2gemini)
that converts the Markdown version of the ChangeLog into Gemtext.

It looks pretty good in Rogallo.

![The Rogallo ChangeLog in Rogallo](/attachments/2026/07/19/rogallo-changelog.webp#centre)

Initially, I set all of this up so that I was editing the files via
[Tramp](https://www.gnu.org/software/tramp/). This worked fine and got me
going, but pretty quickly I decided that it would make more sense to [create
a repository](https://github.com/davep/tilde-team-capsule), edit stuff
locally, and then just `rsync` it when I'm good to go.

Not editing in production... I know... How boring.

[//]: # (2026-07-19-some-documentation-in-geminispace.md ends here)
