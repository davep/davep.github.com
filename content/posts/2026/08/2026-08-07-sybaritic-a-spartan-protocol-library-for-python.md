---
title: "Sybaritic - A Spartan protocol library for Python"
date: "2026-08-07 19:27:00+0100"
category: Python
tags: [Coding, PyPI, Python, Rogallo, "Spartan Protocol", smolweb, sybaritic]
---

Now that [Rogallo](https://rogallo.davep.dev/) supports [multiple
protocols](https://rogallo.davep.dev/protocols/), it's tempting to add one
or two more. As of the time of writing, alongside
[Gemini](https://rogallo.davep.dev/gemini/), both
[Gopher](https://rogallo.davep.dev/gopher/) and
[Finger](https://rogallo.davep.dev/finger/) are supported. While wandering
the [small web](/tag/smolweb/), I stumbled on [the Spartan
protocol](https://github.com/michael-lazar/spartan). Given its similarity to
Gemini and the fact it uses [Gemtext](/tag/gemtext/) as its main document
type, adding it to Rogallo seemed like an obvious thing to do.

In aid of this, I've created [Sybaritic](https://sybaritic.davep.dev/). It
is, in effect, a sibling library to [Wasat](https://wasat.davep.dev/),
[Port70](https://port70.davep.dev/) and [Port79](https://port79.davep.dev/).
As with the others, it is async-all-the-way and is designed to have a
similar API.

With this in place, I can now extend Rogallo to handle `spartan://` URIs as
first-class citizens.

[//]: # (2026-08-07-sybaritic-a-spartan-protocol-library-for-python.md ends here)
