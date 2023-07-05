---
layout: post
title: Build in public, even in private
categories: []
tags: programming
date: 2022-10-06 10:44:00 +0100
---

As mentioned [yesterday](/2022/10/05/on-to-something-new-redux.html), I'm
about to start working at [Textualize](https://www.textualize.io), and
building Open-source software is important to the company.
[Will](https://twitter.com/willmcgugan) -- the CEO -- is all about building
in public. If you follow him on Twitter you'll notice that his Python coding
adventure tweets actually outnumber is cooking tweets!

As someone who has long been a supporter of and fan of [Free
Software](https://www.gnu.org/philosophy/free-sw.en.html) and [Open-source
software](https://en.wikipedia.org/wiki/Open-source_software), and has made
some small contributions along the way, I've also always made a point of
[building my own tools in public](https://github.com/davep/). In most cases
they're things that are likely only helpful to me, but some are more
generally useful. The point being though: it's all there in case it's
helpfull to someone else.

Which means that, as much as possible, when I'm writing code, I write it as
if it's going to be visible in public and someone else is going to be
reading it. I try and make the code tidy. I try and comment it well. I try
(but don't always manage for personal projects) to fully document it. The
important thing here being that someone coming to the code fresh should be
able to follow what's going on.

Against that background, and having just gone through the process of handing
off almost 5 years of work to someone else as a left an employer, I got to
thinking: we should always "build in public", even if it's in private.

When I started with my previous employer, and even to the day I left, I was
the only software developer there. I worked with a team who wrote code, but
being software developers wasn't what they did. Bioinformaticians and
machine learning scientists have other things to be doing. But, as I wrote
my code, I wrote every line assuming they, or some other developer down the
line, would be reading it. Pretty much every line was written for an
audience I couldn't see and didn't fully know. This, as mentioned above,
meant trying to keep the code clean, ensuring it was commented in helpful
ways, ensuring the documentation was helpful, and so on.

But it wasn't just about the code. Any non-trivial system will have more to
it than code. We had an internal instance of GitLab and I tracked all of my
work on there. So, as I planned and worked on new features, or went on bug
hunts, I'd document the process in the issue tracker. As much as possible
I'd be really verbose about the process. Often I wouldn't just open an
issue, go work on it, and then mark it closed; as I worked through the issue
I'd add comment after comment under it, documenting my thinking, problems,
solutions, cite sources when looking something up, that sort of thing.

The whole process was an act in having a conversation with current or future
team members if they ever needed to look; with future me (really, that
helped more than once -- we all have those "that the *hell* was I thinking?"
moments); with any developer(s) who took over from me in the future.

I did all this as if I was broadcasting it in public [on
Twitter](https://twitter.com/davepdotorg) or [on
GitHub](https://github.com/davep), etc. It was in private, of course, but I
approached it as if it was in public.

There were always three main reasons for this, I felt:

1. Accountability. At any moment someone who I worked with could review what
   I was doing and why I was doing it; it was an invitation to anyone
   curious enough to talk with me about what I was building and how I was
   building it.
2. Continuity of support for unplanned reasons. Life happens, sometimes you
   may, unplanned, never be available at work again. I never wanted to leave
   my employer in a position where picking up from such an event was a
   nightmare.
3. Continuity of support for planned reasons. It was possible, and it became
   inevitable, that I'd move on to something else. If that was to happen I
   wanted to be sure that whoever picked up after me would be able to do so
   without too much effort.

In the end item 3 seemed to really pay off. When it came time for me to hand
over my work to someone else, as I left, the process was really smooth and
trouble-free. I was able to point the developer at all the documentation and
source code, at all the issues, and invite them to read through it all and
then come back to me with questions. In terms of time actually spent talking
about the main system I was handing over I'd say that 4 years of work was
handed over with just a few hours of actual talking about it.

It remains to be seen if it really paid off, of course. If they get really
stuck they do have an open invitation to ping me a question or two; I care
enough about what I designed and built that I want it to carry on being
useful for some time to come. But... I like to think that all of that
building in public, in private, will ensure that this is an invitation that
never needs to be called on. I like to think that, if something isn't clear,
they'll be able to check the code, the documentation and the issue history
and get to where they need to go.

[//]: # (2022-10-06-build-in-public-even-in-private.md ends here)
