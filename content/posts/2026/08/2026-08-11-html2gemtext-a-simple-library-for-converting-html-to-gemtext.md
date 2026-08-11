---
title: "html2gemtext - A simple library for converting HTML to Gemtext"
date: "2026-08-11 20:24:39+0100"
category: Python
tags: [Coding, "Gemini Protocol", PyPI, Python, gemtext, smolweb]
---

Yesterday evening, while tinkering with
[Rogallo](https://rogallo.davep.dev/), I managed to nerd-snipe myself pretty
well. I was playing around with the idea of better presentation of some
forms of `text/*` content. While, of course, Rogallo handles `text/gemtext`
just fine, there are lots of other MIME types that it will show too (pretty
much all within `text/*`). Already, if it can work out an appropriate
language, the viewer will do syntax highlighting, and this includes Markdown
files. However, [Rogallo has a full Markdown widget built right
in](https://textual.textualize.io/widgets/markdown/) so I was experimenting
with using that as the way to show Markdown content.

Nothing that clever really, all pretty obvious.

But then I got to thinking... In [OldNews](https://oldnews.davep.dev/) I
heavily rely on
[`html-to-markdown`](https://docs.html-to-markdown.xberg.io/). Given I have
a Markdown viewer to hand, if the user ends up trying to look at some
`text/html`, why not convert it over to Markdown and render it that way?
That's... doable.

There are, however, some problems with this idea:

- As useful as `html-to-markdown` has been for OldNews, I've found it quite
  unreliable at times, with the occasional breaking change. I don't mention
  this as a negative about the project, but I don't want another one of my
  projects sitting on top of a moving target like that.
- Dragging in a reasonably large dependency for what's likely to be a niche
  requirement doesn't quite feel right.
- Textual's Markdown viewer has, to this day, one massive design flaw: links
  can't be navigated with the keyboard[^1]. I'm doing my absolute best to
  ensure that Rogallo is keyboard-first. Leaning on this widget for viewing
  Markdown is one thing, but leaning on the widget for other content types
  starts to erode that aim.

I did consider the idea of having this feature as an install option, so
you'd be able to install `rogallo` and have it work as normal, or install
`rogallo[html]` (or similar) and it would drag in the ability to render some
HTML using this pipeline.

Then I realised: why target Markdown at all? I already have the code for
rendering Gemtext, and that solves the keyboard navigation of links problem.
How hard could it be to write something to convert HTML to Gemtext?

Turns out, at least for the requirements I have right now, [not that
hard](https://github.com/davep/html2gemtext)!

[`html2gemtext`](https://html2gemtext.davep.dev/) is still in its infancy,
but it's doing a passable job of turning most of the HTML I throw at it into
reasonable Gemtext. I don't doubt for a moment that there are *lots* of
pages out there that won't turn out right -- for varied values of right --
but so far the results are readable and navigable. The plan now is to keep
improving as I run into new cases that could be handled better.

While I've not built this into Rogallo just yet, I think I will make use of
it. I'm also giving serious thought to using it for [my
capsule](gemini://tilde.team/~davep/). Over there I'm [adding some posts
from this blog](gemini://tilde.team/~davep/gemlog/) and `html2gemtext` could
form the basis of a tool to help automate some of that.

Right now [I'm using a script I've
written](https://github.com/davep/tilde-team-capsule/blob/11a6bfa7e0ab6015471d660cacdd0287d10bd3dc/bin/borrow-from-blog)
that wraps [`lowdown`](https://kristaps.bsd.lv/lowdown/) to do the Markdown
to Gemtext conversion, but the result -- as good as it is -- isn't *quite*
what I'd like. I'm thinking I could tailor the results exactly as I want if
I go from this blog's HTML via `html2gemtext`.

Or, of course, given my blog is written in Markdown, I could next tackle my
own just-how-I-need-it Markdown to Gemtext converter...

As for how this new library will go into Rogallo... Using it to render HTML
that might be found kicking about in Geminispace or Gopherspace makes sense,
I think. That should be enough. It's not like I *really* need to turn it
into an `http(s)` browser too. Right? Right?!?

[^1]: This mouse-only problem is a recurring theme in Textual.

[//]: # (2026-08-11-html2gemtext-a-simple-library-for-converting-html-to-gemtext.md ends here)
