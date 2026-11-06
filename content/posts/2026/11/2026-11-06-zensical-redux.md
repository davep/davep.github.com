---
title: "Zensical (Redux)"
date: "2026-11-06 10:53:24+0000"
category: Coding
tags: "GitHub, Zensical, documentation, gh-pages, mkdocs, mkdocstrings"
---

Back in March this year [I dipped my toe into trying out
Zensical](/2026/03/06/zensical.html) as a replacement for
[MkDocs](https://www.mkdocs.org)/[mkdocs-material](https://squidfunk.github.io/mkdocs-material/).
At the time I had success with using it as a drop-in replacement for a
project, and following that used it for a couple more. All was good.

In that post, towards the end, I also said:

> The next test will be to try [the docs for something like
> Hike](https://hike.davep.dev/). They're a little bit more involved, with
> [SVG-based screenshots being generated at build
> time](https://github.com/davep/hike/blob/f5748ee97ee2e6928c08f28b1fb4e6e607db6b5e/docs/source/index.md#L3-L4),
> etc. If that just works out of the box too, without incident, I think I'm
> all sorted.

I did [try this](https://github.com/davep/hike/pull/152), but ran into a
problem: the screenshots took **ages** to build. At that point I decided to
put the PR on the back-burner and only use [Zensical](https://zensical.org/)
for more static-like sites.

A couple of days ago I noticed that [v0.1.0 had been
released](https://github.com/zensical/zensical/releases/tag/v0.1.0), and
with it this claim:

> This release closes the major remaining compatibility gaps with MkDocs,
> including support for many of its most widely used plugins. You can bring
> your existing MkDocs project to Zensical and continue using the workflows
> you're familiar with.

With this I was reminded that I'd not gone back and tried to use it again.
So I took the Hike PR, upgraded Zensical, rebuilt the docs and... pretty
much as fast as MkDocs! The result, style changes aside, looked the same
too.

Given that it seemed to be working fine, I decided to start again from
scratch with my current pet project of choice:
[Rogallo](https://rogallo.davep.dev/). I removed MkDocs/mkdocs-material,
added Zensical, tweaked the `Makefile`, ran [`make
rtfm`](https://github.com/davep/rogallo/blob/a7fc51253c94e1668348e3989b6d6dc14c8fc730/Makefile#L112-L114)
and... crash! The error being along the lines of:

```
RuntimeError: Python error: FileNotFoundError: [Errno 2] No such file or directory: '[...]/site-packages/zensical/templates/.icons/simple/cplusplus.svg'
```

I tweaked a couple of things to eliminate anything particular about my
environment (in the case of Rogallo,
[SmolServe](https://smolserve.davep.dev/) is used to [run
Zensical](https://github.com/davep/rogallo/blob/a7fc51253c94e1668348e3989b6d6dc14c8fc730/Makefile#L18-L20),
to ensure there's a test server available for making the screenshots, so I
wanted to ensure that it wasn't some fallout from that setup), but the
problem remained.

I then hit [the
issues](https://github.com/zensical/zensical/issues?q=sort%3Aupdated-desc+is%3Aissue+state%3Aopen+)
and did a quick search; [it turned out it was a known
issue](https://github.com/zensical/zensical/issues/1111) and, in my case,
was easily fixed with a quick [`make
update`](https://github.com/davep/rogallo/blob/a7fc51253c94e1668348e3989b6d6dc14c8fc730/Makefile#L64-L66)
(resolving the issue that `markdown-exec` had a small bug that had
subsequently been addressed).

So, as of today, [I've swapped Rogallo over to using Zensical for its
documentation](https://github.com/davep/rogallo/pull/504) and, so far, it
looks to be working out well. From my perspective the claim of it being a
drop-in replacement is 100% true.

My only quibble: I wish they supported a `zensical.yml` configuration file.
From what I can tell [it's `zensical.toml` or
`mkdocs.yml`](https://zensical.org/docs/setup/basics/), so no satisfying
`mv mkdocs.yml zensical.yml` to be had here.

I think I can cope with that, though.

[//]: # (2026-11-06-zensical-redux.md ends here)
