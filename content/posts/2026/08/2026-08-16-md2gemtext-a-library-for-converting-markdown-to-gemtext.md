---
title: "md2gemtext - A library for converting Markdown to Gemtext"
date: "2026-08-16 14:43:04+0100"
category: Python
tags: [Coding, "Gemini Protocol", Markdown, PyPI, Python, gemtext, md2gemtext, smolweb]
---

Following on from
[html2gemtext](/2026/08/11/html2gemtext-a-simple-library-for-converting-html-to-gemtext.html),
the inevitable has happened: I couldn't let the Markdown side of things
remain unaddressed. While [Rogallo](https://rogallo.davep.dev/)
[v1.8.0](https://rogallo.davep.dev/changelog/#v180) added some extra
rendering of Markdown to make it look more "pretty", I felt it really needed
to be handled so it had more utility. Being fully navigable, even by
keyboard, seems more important than pretty tables.

So [md2gemtext](https://md2gemtext.davep.dev/) now exists as a library on
[PyPI](/tag/pypi/). I have two plans for this. While I fully intend to shake
up the Markdown support in Rogallo -- either replacing the use of the
Textual Markdown widget to display it, or at least giving the user a
configuration option to decide how Markdown is displayed -- I also want to
pay some attention to my (currently rather simple) [Gemini-based
log](gemini://tilde.team/~davep/gemlog/) and use this library to build a
tool that will convert this blog's [Markdown
content](https://github.com/davep/davep.github.com/tree/main/content/posts)
into Gemtext that looks just how I want it.

As with html2gemtext, this is an early version of this library, and I'm sure
there will be edge cases I'll have missed and will want to tidy up. But at
the moment the results are looking promising.

I'm once again in a place where I'm actually half-seriously thinking that
much of what [Hike](https://hike.davep.dev/) does could be built into
Rogallo, if I were to simply add `http(s)` support there.

[//]: # (2026-08-16-md2gemtext-a-library-for-converting-markdown-to-gemtext.md ends here)
