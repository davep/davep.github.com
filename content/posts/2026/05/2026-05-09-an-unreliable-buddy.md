---
title: An unreliable buddy
date: 2026-05-09 19:14:23+0100
category: AI
tags: BlogMore, Coding, Copilot, Gemini, GitHub, Google, Python, code review, code smell
cover: /attachments/2026/05/09/rate-limit.webp
---

At some point this morning I was looking for something on this blog and
stumbled on a post that had a broken link. Not an external link, but an
internal link. This got me thinking: perhaps I should add some sort of
linting tool to [BlogMore](https://blogmore.davep.dev/)? I figured this
should be doable using much of the existing code: pretty much work out the
list of internal links, run through all pages and posts, see what links get
generated, look for internal links[^1], and see if they're all amongst those
that are expected.

Later on in the day [I prompted Copilot to have a
go](https://github.com/davep/blogmore/issues/465). Now, sure, I didn't tell
it *how* to do it, instead I told it what I wanted it to achieve. I hoped it
would (going via Claude, as I've normally let it) decide on what I felt was
the most sensible solution (use the existing configuration-reading,
page/post-finding and post-parsing code) and run with that.

It didn't.

Once again, as I've seen before, it seemed to understand and take into
account the existing codebase *and then copy bits from it and drop it in a
new file*. Worse, rather than tackle this using the relevant parts of the
existing build engine, it concocted a whole new approach, again obsessing
over throwing a regex or three at the problem.

I then spent the next 90 minutes or so, testing the results, finding false
reports, finding things it missed, and telling it what I found and getting
it to fix them. It did, but on occasion it seemed to special-case the fix
rather than understand the general case of what was going on and address
that.

Eventually, probably too late really, I gave up trying to nudge it in the
right direction and, instead, decided it was time to be more explicit about
how it should handle this[^2]. The first thing that bothered me was that it
seemed to ignore the configuration object. Where BlogMore has a method of
loading the configuration into an object, which can be passed around the
code, but with the linter it loaded it up, pulled it all apart, and then
passed some of the values as a huge parameter list. Because... reasons?

Anyway, I told it to cut that shit out and prompted it about a few other
things that looked pretty bad too. Copilot/Claude went off and worked away
on this for a while, using up my 6th premium request of the session, and
then eventually came back with an error telling me I'd hit a [rate
limit](https://docs.github.com/copilot/concepts/rate-limits) and to come
back in a few hours.

![GitHub rate limit](/attachments/2026/05/09/rate-limit.webp#centre)

Could I have got it to where I wanted to be a bit earlier, with more careful
prompting? No doubt. Will a lot of people? I suspect that's rather unlikely.
This is one of the many things that make me pretty sceptical about this as
the tool some sell it as, at least for the moment. I see often that it's
written about or talked about as if it's a really useful coding buddy. It
can be, at times, but it's hugely unreliable. Here I'm testing it by
building something as a hobby, and I'm doing so knowing that there's no real
consequence if it craps out on me. I'm also doing it safe in the knowledge
that I could write the code myself, albeit at a far slower pace and with
less available time. Not everyone this is aimed at has that going for them.

But these tools are still sold like they're the most reliable coding buddies
going.

All that said: having hit the rate limit, and having squandered six premium
requests on the problem with no real progress, I decided to use my Google
Gemini coding allowance instead (which, in my experience so far, seems
pretty generous). I threw more or less the same initial prompt at it, but
this time I stressed that I really wanted it to use the existing engine
where possible. It managed to pretty much one-shot the problem in about 9
minutes and used up just 2% of [my daily
quota](https://geminicli.com/docs/resources/quota-and-pricing/)[^3].

I've done a little more tidying up since, and I still need to properly
review [the result](https://github.com/davep/blogmore/pull/467), but from
what I can see of the initial results it's found all of the issues I wanted
it to find, first time (something Claude didn't manage) and hasn't found any
issues that don't exist (also something Claude didn't manage).

So I guess this time Gemini was the reliable buddy. But not knowing which
buddy you can rely on makes for a pretty unreliable group of buddies.

[^1]: This process could, of course, work for external links too, but I'm
    not really too keen on having a tool that visits every single external
    link to see if it's still there.
[^2]: Which is mostly fine; I'm doing this as an experiment in what it's
    capable of, and also I was sofa-hacking while having a conversation
    about naming Easter eggs in Minecraft.
[^3]: Imagine that too! Imagine knowing exactly how much of your quota
    you've used at any given moment! Presumably GitHub don't show you where
    you are in respect to the rate limits on top of your monthly quota
    because grinding to a halt with no warning is more... fun?

[//]: # (2026-05-09-an-unreliable-buddy.md ends here)
