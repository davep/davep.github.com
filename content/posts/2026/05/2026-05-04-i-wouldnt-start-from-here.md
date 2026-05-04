---
title: I wouldn't start from here
date: 2026-05-04 20:59:18+0100
category: AI
tags: BlogMore, Coding, Copilot, Gemini, GitHub, Google, Python, code review
---

The tidying of the [BlogMore](https://blogmore.davep.dev/) source carries
on; sometimes by hand, but also sometimes by using either Copilot/Claude or
Gemini to decide how best to nudge the codebase in a desired direction. When
I do the latter, if I like the suggestions the agents make, but it looks
like a bunch of work and I can't be faffed with all that typing, I get them
to do the work; otherwise, I'll do it myself.

I am, however, seeing lots of evidence of what I expected to happen, and
anticipated happening: to get to where I would like the code to be, I
wouldn't have started here.

I'll stress again, for anyone who hasn't been following along, for anyone
who might have landed into the middle of this [long thread of AI
experimenting](/category/ai/), that this was the point and purpose. I wanted
to use this tool to build something relatively inconsequential, and which I
could likely build myself given the time and the inclination, and also
something I would actively use.

So where am I at? My main distaste at the moment is the core generation
code. Just a few days ago this was a couple of thousand lines of repetitive
code that did the job, but which was a bit messy. There's no question that I
would not have written it anything like this. Because of this I've been on a
push to try and break it up and tidy it up. While doing this I've been
playing Copilot/Claude and Gemini off against each other, to see who does
what.

As of the time of writing, the generator is split up, but in a way I
wouldn't have done myself either. It's pretty much half a dozen mixin
classes in a trench coat, all pretending to be one cohesive class. I *feel*
that's a reasonable solution given where I started, but honestly I wouldn't
have started there had I been coding this by hand.

Right at the moment I'm working out the best way forward to tidy up an
outcome of this approach that I really don't like. The generator code is
littered with lots of `# type: ignore[attr-defined]` to keep `mypy` happy,
because that's what Claude did when it built all those little mixins. To
borrow from the explanation in `AGENTS.md`, the current makeup looks like
this:

```
MinifyMixin
  └── AssetsMixin          (adds icons, file copying)

DateArchivesMixin
  └── ListingMixin         (adds tag/category listings)

OptionalPagesMixin
  └── PagesMixin           (adds core post/page/index/archive)

SiteGenerator(
    AssetsMixin, ContextMixin, GroupingMixin,
    ListingMixin, PagesMixin, PathsMixin
)
```

The issue is (for example) that `MinifyMixin` defines a method
`_write_html`. Meanwhile `OptionalPagesMixin` and `ListingMixin` and so on
make use of `self._write_html`. But because there's no direct connection
between those two classes and `MinifyMixin`, `mypy` complains that
`_write_html` isn't defined. Of course, it *isn't* defined, because it only
becomes available when all those classes climb into the `SiteGenerator`
trench coat and pretend to be a real class.

The `ignore` direction solves the problem, but it's ugly and it's cheating.

So I then set the two different agents on the path of proposing a solution
to this. Both were quite different. Claude (via Copilot) decided that an
abstract base class was the solution. Gemini decided that a protocol was the
solution. I *think* I'm siding with Gemini on this one because this is a
provides/needs problem, not a "kind of" problem. Even then though, while I
sense Gemini has the right approach, I'm not always happy with its
implementation of it[^1], and once again: it's a cleanup of something I'd
sooner not be cleaning up in the first place.

So here's the thing, and this harks back to [wondering if the code is that
bad](/2026/04/26/but-is-the-code-that-bad.html): it isn't... but it's also
generating work *if* you look at the code and decide that you want it clean
and maintainable.

To get to where I want to go, I wouldn't start from here.

I get why I'm seeing the odd report here and there of people abandoning
their code bases, or deciding to rebuild them from scratch by hand. Part of
me wants to start a fresh branch, remove almost everything, and rewrite the
code so it has feature-parity but in a way where I feel the code is tidy and
elegant.

The experiment is working as planned.

[^1]: And it feels so slow. SO. SLOW!

[//]: # (2026-05-04-i-wouldnt-start-from-here.md ends here)
