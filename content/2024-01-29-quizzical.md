---
layout: post
title: Quizzical
category: Coding
tags: Python, terminal, textual
date: 2024-01-29 21:30:00 +0000
cover: attachments/2024/01/29/quizzical-banner.png
---

I feel like I'm on a bit of a roll when it comes to building applications
for the terminal at the moment; while I'm still tinkering and improving
[tinboard](https://github.com/davep/tinboard) and
[OSHit](https://github.com/davep/oshit), I had the urge to tackle another
idea that's been on my TODO list for a while.

This is something [I did for Emacs](https://github.com/davep/quiz.el) back
in 2017 and I felt it was a *perfect* candidate for a Textual-based project.
It's a terminal-based trivia quiz game, using [the Open Trivia
Database](https://opentdb.com/) as the source of questions.

![Quizzical](/attachments/2024/01/29/quizzical.png#centre)

I've just published an early version [to
PyPI](https://pypi.org/project/quizzical/); it still needs some polish and I
have a few other ideas for it, but as it stands I feel it's a fun little
game to mess around with.

The idea is pretty straightforward: you can run it up and create lots of
different quizzes, there are various parameters you can use to create lots
of different kinds of challenges:

![Building a new quiz](/attachments/2024/01/29/new-quiz.png#centre)

Once you're created a quiz, you can run it and answer away:

![An example question](/attachments/2024/01/29/question.png)

Right now the idea is that you answer by pressing either <kbd>1</kbd>,
<kbd>2</kbd>, <kbd>3</kbd> or <kbd>4</kbd> (or just <kbd>1</kbd> or
<kbd>2</kbd> for true/false questions); when I get a moment I'll also enable
mouse support for selecting an answer too (honestly I feel
keyboard-answering feels far more natural).

Once the quiz is done you can review your answers and see which were right
and which were wrong:

![Viewing results](/attachments/2024/01/29/results.png#centre)

As I say: there's a bunch of other things I want to add to this (keeping
track of scores, adding session token support to reduce the chances of
repeat questions, etc), but this felt like a good spot to make a v0.1.0
available if anyone else wanted to have a play.

Anyway, if this sounds like your sort of thing, it can be installed with
`pip` or (ideally) `pipx` [from PyPi](https://pypi.org/project/quizzical/).
The [source is available over on
GitHub](https://github.com/davep/quizzical).

PS: Now you can see why I made
[`textual-countdown`](/2024/01/11/textual-countdown.html).

[//]: # (2024-01-29-quizzical.md ends here)
