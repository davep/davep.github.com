---
title: And then there were three
date: 2026-05-05 12:37:53+0100
category: AI
tags: BlogMore, Coding, Copilot, Gemini, GitHub, Google, Python, code review, code smell
cover: /attachments/2026/05/05/three-prs.webp
series: Agentic Afterthoughts
---

Given the concerns [I wrote about
yesterday](/2026/05/04/i-wouldnt-start-from-here.html), in regard to the
core generation code in [BlogMore](https://blogmore.davep.dev/), I've been
thinking some more about how I *would* probably have the code look. First
thing this morning, over breakfast and coffee, I concluded that I'd probably
have gone with something that was a single orchestration function/method,
into which would be composed some modular support code. Back when I [started
the process of breaking up the generator](/2026/05/03/a-stroppy-agent.html)
I seem to recall that Gemini *sort of* went along those lines, but the code
it created seemed pretty messy and the main site generation class was still
a lot bigger than I would have liked. This is why, at the time, I went with
Copilot/Claude's mixin-based approach; it felt a bit more hacky but the code
felt tidier.

With this all in mind, I popped to my desk, made a branch off [the current
Gemini attempt to clean up the typing issues with the mixin
approach](https://github.com/davep/blogmore/pull/452), fired up Gemini CLI,
and wrote it a prompt explaining what I didn't like and what I wanted it to
do. The key points being:

- I wanted a similar separation of concerns as the mixin approach was aiming
  for.
- I wanted to move away from mixins.
- I wanted to favour something closer to composition.
- I wanted to favour simple functions over classes where possible.

I then set it off working and left it to get on with things. Overall I think
it took around an hour, with the need for me to approve things now and again
(so probably could have been faster, I wasn't there to answer right away
every time), but it got there in the end. This has [resulted in a third PR
to clean up the generator typing
issues](https://github.com/davep/blogmore/pull/453). In doing so I feel I've
also addressed most of the unease I was feeling yesterday evening, and might
actually have got closer to where I'd rather the code was.

Glancing over the result, I can still see things I'd want cleaned up, and
done in a slightly different way, but overall I have a better feeling about
this third approach. I sense this is a better place to move on from.

![Three PRs](/attachments/2026/05/05/three-prs.webp#centre)

So that's three PRs I have lined up to address [the code smell that's been
bugging me for a couple of
days](https://github.com/davep/blogmore/issues/447). One fixes it with an
ABC; one fixes it with a protocol; and now one fixes it by reworking the
submodularisation of the generator to use a different approach entirely. On
the one hand, this seems like a lot of work and a lot of faff (and, as I
said yesterday, I wouldn't start here to get where I want to be), but on the
other hand I do kind of understand the appeal of being able to get hours of
work done in a relatively short period of time, so you can experiment with
the results.

Would I recommend someone work this way? No, of course not. Does it make for
an interesting side-quest when I'm in *"it is still my hobby too"* mode?
Yeah, it does.

[//]: # (2026-05-05-and-then-there-were-three.md ends here)
