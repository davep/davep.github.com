---
title: Gemini is kind of messy
date: 2026-05-14 08:25:23+0100
category: AI
tags: AI, Coding, Gemini, Google
---

As I've mentioned a few times recently, I'm using Google's [Gemini
CLI](/tag/gemini/) more at the moment; in part because I have a Gemini Pro
account so it makes sense to use it, but also [in anticipation of dropping
anything to do with Copilot](/2026/05/13/the-copilot-bait-and-switch.html).

While I've had some troubles with it -- as can be seen
[here](/2026/05/03/a-stroppy-agent.html),
[here](/2026/05/12/the-other-unreliable-buddy.html) and
[here](/2026/05/13/when-gemini-cli-gets-stuck.html) for example -- I'm
mostly having an okay time. The code it writes isn't too bad, and while it
seems to need a little more direction and overseeing than I've been used to
while using Copilot/Claude, it generally seems to arrive at sensible
solutions for the problems I'm throwing at it[^1].

One difference with working with Copilot CLI that I *have* noticed, however,
is that Gemini doesn't seem to care for cleaning up after itself. When faced
with a problem it'll often write a test program or two, perhaps even create
a subdirectory to hold some test data, run the tests and be sure about the
outcome. This is good to see. It's not unusual for me to do this myself (or
at least in the REPL anyway). But it really doesn't seem to care to actually
clean up those tests. A handful of times now I've had it leave those files
and directories kicking around. I've even said to it *"please clean up your
test files"* and it's gone right ahead and done so, which suggests it
"knows" what it did and what it should do.

This also feels like a new source of mess for all the people who commit
their executables and the like to their repositories. That should be fun.

The thing I don't know or understand, at least at the moment, is if this is
down to the CLI harness itself, or the choice of model, or a combination of
both, or something else. I'm curious to know more.

[^1]: There is a weird thing I'm seeing, which I want to try and properly
    capture at some point, where it'll start tinkering with unrelated code,
    I'll undo the change, it'll throw it back in the next go, I'll undo,
    rinse, repeat...

[//]: # (2026-05-14-gemini-is-kind-of-messy.md ends here)
