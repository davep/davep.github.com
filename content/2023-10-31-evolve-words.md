---
layout: post
title: Evolve Words
category: Coding
tags: Python, evolution, biology, terminal, textual
date: 2023-10-31 21:39:00 +0100
cover: /attachments/2023/10/31/evolve-words-cover.png
---

This follows on from my [previous post](/2023/10/26/visual-selection.html).
If you've not read that, it's worth having a dive in first for the
background.

The Ruby code I mention, that was written back in 2008, was actually a pair
of scripts. The first one, called `selection`, did what `visual-selection`
does, only `visual-selection` does it with a nice TUI interface: it takes a
random collection of letters and symbols and evolves them into a target
phrase.

As covered before: I don't remember all of the details of the conversation
that was going on at the time, but I do seem to remember something along the
lines of *"yes, but you start out and end up with something the same
length"* and *"nothing more complex is made"* (let's gloss over the whole
"complex" thing for now... well okay let's just gloss over it, end of story;
this is just a fun coding exercise).

What I do remember is that the seed of an idea was planted. Fine: how about
I start off with one small word, and using a list of English words as the
"fitness landscape" that the mutations had to survive in, mutate a
population over and over and see what happens. Would I "randomly" create
known words, with fewer letters, with the same letters, with more letters?

So this version of the code randomly did three forms of mutation: it would
randomly flip a letter, or randomly delete a letter, or randomly insert a
random letter. It would do this over and over and eliminate words that
aren't in the original list (the simple form of selecting for survival
within the landscape).

Like I said last time: never going to convince anyone of anything, but fun
to write some code.

This version became `selection2`.

So, having turned `selection` into a TUI application with Textual, I *had*
to do the same with this code...

![Evolve Words](/attachments/2023/10/31/evolve-words.png#centre)

As before, because it's fun not to do so, this leans heavily on the [worker
API](https://textual.textualize.io/guide/workers/) and
[`textual-plotext`](https://textual.textualize.io/blog/2023/10/04/announcing-textual-plotext/).

If you want to check out the app itself there's [a GitHub
repo](https://github.com/davep/evolve-words) and it can also be
installed [from PyPi](https://pypi.org/project/evolve-words/) using
`pipx`.

[//]: # (2023-10-31-evolve-words.md ends here)
