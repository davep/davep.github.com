---
title: The other unreliable buddy
date: 2026-05-12 08:20:25+0100
category: AI
tags: AI, Coding, Gemini, Google, leadership, quote
---

Having had [Copilot crash out the other
day](/2026/05/09/an-unreliable-buddy.html), while working on the
[linter](https://blogmore.davep.dev/linting/) for
[BlogMore](https://blogmore.davep.dev/), I decided to lean into [Gemini
CLI](https://geminicli.com/) a little more and see how that got on.

When I first tried it out, [a week
back](/2026/05/05/and-then-there-were-three.html), I found it worked fairly
well but could be rather slow at times. On the whole though, I found it easy
enough to work with; the results weren't too bad, even if it could [throw
out some mildly annoying code at times](/2026/05/03/a-stroppy-agent.html).

Yesterday evening though, because of the failure of Copilot, I decided to go
just with Gemini and work on the [problem of speeding up
BlogMore](/2026/05/11/speeding-up-blogmore.html). This worked really well. I
found that it followed instructions well[^1] when given them, and also did a
good job of applying what it was told, constantly, without needing to be
told again. I actually found I had a bit of a flow going (in the minimal way
that you can get any sort of flow going when you're not hand-coding).

Using it, I tackled all the main bottlenecks in BlogMore and got things
working a lot faster (at this point it's generating a site in about 1/4 of
the time it used to take). By the time that work was done, I wanted to do
some last tidying up.

This was where it suddenly got unreliable. I asked it a simple question, not
even tasking it with something to do, and it went into "*Thinking...*" mode
and never came back out of it. I seem to remember I gave it 10 minutes and
then cancelled the request.

After that I tried again with a different question, having quit the program
and started it again with `--resume`. This time I asked it a different
question and the same thing happened. I hit cancel again and then, a moment
later, *finally* got an answer to the previous question.

From this point onwards I could barely ever get a reply out of it. I even
tried quitting and starting up again without `--resume`, only for the same
result.

A quick search turns up reports similar to this issue on Reddit, Google's
support forums and [on
GitHub](https://github.com/google-gemini/gemini-cli/issues/25520). It looks
like I'm not alone in running into this.

This here is one of the things that concerns me about the idea of ever
adopting agents as the primary tool for getting code written: the
unreliability of their availability, and so the resulting inconsistency of
the output. It feels like any perceived win in terms of getting the code
written is going to be lost in the frustration of either waiting and trying
again when it just gives up playing along, or in running from one agent to
another, hoping you find the one that is capable of working with you at that
given moment.

Meanwhile folk talk like it's *the* solution to the problem of software
development. It's especially concerning when those folk are in "engineering
leadership" or a position with a similar name. When they talk like this they
are either displaying a lack of foresight, or betraying a lack of care for
the craft they are supposed to represent (amongst [other
reasons](https://en.wikipedia.org/wiki/Peter_principle)).

It's very timely that [this
post](https://fosstodon.org/@robpike@hachyderm.io/116557976043815089) from
[Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike) popped up in my feed this
morning:

> Although trained in physics, I worked in the computing industry with pride
> and purpose for over 40 years. And now I can do nothing but sit back and
> watch it destroy itself for no valid reason beyond hubris (if I'm being
> charitable).
>
> Ineffable sadness watching something I once loved deliberately lose its
> soul.

Yup.

[^1]: Albeit I sense it pays little to no attention to `AGENTS.md`

[//]: # (2026-05-12-the-other-unreliable-buddy.md ends here)
