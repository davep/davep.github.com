---
layout: post
title: Documentation generation
category: AI
tags: Python, Blogging, AI, LLM, Copilot, GitHub, BlogMore
date: 2026-03-05 16:26:00 +0000
---

While I've written a *lot* of documentation in my life, it's not something I
enjoy. I want documentation to read well, I want documentation to be useful,
I want documentation to be accurate. I also want there to be documentation
at all and sometimes the other parts mean it doesn't get done for FOSS
projects[^1].

When [I started the experiment that is
BlogMore](/2026/02/20/five-days-with-copilot.html), I very quickly [hashed
out some ideas on how it might generate some
documentation](https://github.com/davep/blogmore/pull/100), and the result
was okay. In fact, if anything, it was a bit too much and there was a lot of
repeated information.

So, this morning, before I sat down for the day's work, I [quickly wrote an
issue](https://github.com/davep/blogmore/issues/209) that would act as a
prompt to Copilot to rewrite the documentation. This time I tried to be very
clear about what I wanted where, but also left it to work out all the
details.

[The result](https://github.com/davep/blogmore/pull/210) genuinely impressed
me. While I'll admit I haven't read it all in detail (and because of this
have left the same warning right at the start), on the surface it looks a
lot clearer and feels like a better journey to learning how to use BlogMore.

[blogmore.davep.dev](https://blogmore.davep.dev) hosts the result of this.

I have a plan to work through the documentation and be sure it's all correct
and all makes sense, but if it's as correct and as useful as I think, I
might have to consider the idea of taking this approach more often. Writing
down the *plan* for the documentation and then letting it appear in the
background while I get on with my actual day makes a lot of sense.

I fear I might be warming to these tools, a little bit. :-/

[^1]: Although I've made a point of doing it for almost every one of my
    recent [Textual](/tag/textual/)-based projects.

[//]: # (2026-03-05-documentation-generation.md ends here)
