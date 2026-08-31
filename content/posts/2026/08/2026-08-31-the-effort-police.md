---
title: "The effort police"
date: "2026-08-31 16:11:06+0100"
category: AI
tags: "AI, LLM, FOSS, coding, Free Software"
---

Earlier today I saw a comment on [a post on
BBS](gemini://bbs.geminispace.org/s/Gemini/47847) that was really quite
disappointing. The post itself was announcing a new Gemini client, in this
case a fully-native macOS one called
[MajorTom](https://github.com/acidus99/MajorTom). It's early days for the
project, but it looks fun. It also looks like the author is having a ton of
fun building it.

I can relate. I've been obsessing over building
[Rogallo](https://rogallo.davep.dev/) since June this year and it's been an
absolute blast. I don't see myself getting bored of it any time soon.

The comment that irked me was this:

> Got excited, then I saw the AGENTS.md :(
>
> It’s hard to get excited about new software when everything is just AI
> generated. I miss the old times when you got excited that someone built
> something. Now it’s just someone wrote a prompt to make a computer build
> something.

It comes over like some messed-up Calvinist puritanical work ethic thing.
Yes, I know all the arguments against the use of AI, you'll find that [I
agree with a good few of them](/series/agentic-afterthoughts/); but there's
something wild about this *"you didn't work hard enough to produce the
software I might otherwise consider using so I've dismissed it"* attitude.
I'd say enough with this nonsense, but it's been going on for as long as
I've been writing code and I doubt it'll stop any time soon. At every step
in the evolution of software development there's always been someone, sat on
the sidelines, tutting and judging because someone is using a new tool that
makes it easier or quicker to do a thing.

Yes, we know, [back in our
day](https://www.youtube.com/watch?v=iEIApUNVBKg)...

What also bothers me is how easily the author of the comment belittles and
diminishes the work of the author of the application. Sure, there are some
folk who will try and one-shot something with a prompt or two, and who might
then pass it off as something carefully considered and designed; but it's
unfair, perhaps even dishonest, to attribute that to someone when you don't
know what process they've gone through.

If I look at Rogallo, for example... AI has been involved along the way. To
be clear: 100% of Rogallo is hand-written code, AI has not been involved in
writing any of it. I *have* used Antigravity as an occasional rubber duck to
hash out some ideas, but there's zero chance I'd let it anywhere near the
code itself[^1]. On the other hand, some of the protocol-based support
libraries I've built have heavily involved AI. Even then, I didn't just slap
in a prompt and run with the result. I did research, I followed the docs, I
read more and more about Gemini and Spartan and Nex, etc. I used an agent to
get the code going based on my understanding of the source material and I
then used that code to support the main work I *actually* wanted to be
doing.

> [!note]
> Thinking about it, here's roughly how it breaks down in terms of actual
> *code written*, so far:
>
> - Rogallo: zero AI
> - bagofstuff: pre-existing but zero AI
> - gemtext: zero AI
> - gophermap: zero AI
> - html2gemtext: zero AI
> - md2gemtext: mostly AI
> - port1900: mostly AI
> - port70: mostly AI
> - port79: mostly AI
> - sybaritic: mostly AI
> - textual_enhanced: pre-existing but zero AI
> - textual_fspicker: pre-existing but zero AI
> - wasat: mostly AI

There's zero chance I could have built Rogallo and all the support code from
a position of ignorance. None of it was "just a prompt". Looking at what's
gone into MajorTom so far, I doubt that's the case there either.

Anyway, back to the main topic...

I also find an element of entitlement in this comment. It reminds me
somewhat of [the person who felt they were owed something by FOSS
authors](/2026/03/10/you-get-what-you-pay-for.html). Excitement is not
something a FOSS author owes you. You are, of course, welcome to go looking
for excitement, but if something you discover doesn't do it for you... it's
not for you, move on, go find something else. Announcing that *you* didn't
get excited because someone else got creative in a way you don't approve of
just makes you look like you want to centre the discussion around you.

Someone made a thing. Someone shared a thing. Someone posted a thing. You
turned up and made it about you. That's kind of rubbish. Don't do that.

It's totally fine to not like the use of AI. It's totally fine to want to
avoid anything built with AI or which is somewhat AI-adjacent. I get it:
it's good to have your own standards and to stick to them. I would suggest,
however, that it starts getting problematic when you need to tell someone
having fun with their own free time that they're not doing so in a way that
meets your standards. Doing that is kind of weird.

Doing that makes you look like the effort police.

[^1]: I've yet to see an agent write Textual code I'd consider reasonable.

[//]: # (2026-08-31-the-effort-police.md ends here)
