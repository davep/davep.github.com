---
title: "Wasat - A Gemini protocol library for Python"
date: "2026-06-17 19:35:29+0100"
category: Python
tags: [AI, Antigravity, Coding, "Gemini Protocol", PyPI, Python, smolweb, wasat]
---

I can't remember how and where I saw it, but just over a week ago I ran into
[Project Gemini](https://geminiprotocol.net/). Somehow I've never read or
seen anything about this before, which is pretty wild considering it's been
on the go for around seven years now. As I read up on it I got more and more
intrigued. I had the urge to do... something with it.

I think the thing I want to do, and I know [I'm far from the
first](https://geminiprotocol.net/software/), is write a client for the
terminal. I'm envisioning something very similar to
[Hike](https://hike.davep.dev/), but obviously only targeting the [`gemini`
protocol](https://geminiprotocol.net/docs/protocol-specification.gmi)
itself, and only handling and rendering
[gemtext](https://geminiprotocol.net/docs/gemtext-specification.gmi).

I will, obviously, be looking to write this in [Python](/tag/python/), and
of course, will be looking to use [Textual](/tag/textual/), which means that
it would be useful to have a Python client library for the protocol, and
ideally a client library that is async. I did some searching, found client
libraries, but none of them seemed to be async-first.

With this in mind, and to kick-start the project, last night I fired up
[Antigravity](/tag/antigravity/)[^1] and got a library up and going.
[Wasat](https://wasat.davep.dev/) is the result. For the moment this should
be considered alpha-status software (hence v0.0.1). I've done some *very*
rudimentary testing and experimenting with it and, so far, so good. It's
also proving to be a good tool with which to get to know the protocol. It
also gives me another project to use to experiment with an agent (this being
the first project I've started from scratch using Antigravity).

Over the next few days I'm going to toy with the library more, clean up the
code, look for any issues, and then I'll start on the client application.
That will be hand-built; no AI. I have some ideas of fun things I want to
do, especially when it comes to handling gemtext.

It'll be nice to have a new pet project that's a hand-coded project. The
first significant one since [OldNews](/tag/oldnews/).

Getting back to Wasat itself: I believe it has everything necessary to allow
for writing such a client (which, to be fair, isn't much -- that's kind of
the point of the protocol). It also comes with a simple CLI built in, which
can be run with `python -m wasat` (if it's just installed as a library) or
with `wasat` (if installed globally, along with any command scripts). The
command itself is just a simple download tool for a "page" in a "capsule".
For example, I can grab the content [of a test capsule I've
created](gemini://davep.gemcities.com/):

```text
$ wasat gemini://davep.gemcities.com/
# Introduction
Hey! I'm Dave. Normally you'd find me at:
=> https://www.davep.org My web site
or
=> https://blog.davep.org My blog
amongst other places. But I discovered Gemini and I'm really curious about
the idea, so here I am giving GemCities a go to get to know things a little
better.
```

(with thanks to [GemCities](https://gemcities.com/) for providing a neat
little service).

As for where this is all going: there's no direction, really. I've found a
neat new thing that I didn't know about before, the idea sits well with me,
and I want to explore it more. It also gives me an excuse to do a thing I
really enjoy doing: writing terminal-based TUI applications for the sake of
it, and especially writing one that works just how I want.

[^1]: No, not [that one](https://xkcd.com/353/), the [other one](https://antigravity.google/).

[//]: # (2026-06-17-wasat-a-gemini-protocol-library-for-python.md ends here)
