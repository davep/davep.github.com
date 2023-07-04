---
layout: post
title: "Going on a journey"
categories: []
tags: [ "python" ]
date: 2019-11-10 14:32:00+0000
---

It's hardly a revelation to say that learning a new programming language, or
even learning software development at all, is even more difficult if you
don't have an actual problem to solve. I know I'm not alone in having pet
projects that, when faced with a new environment, I'll code up a version of
that project as a way to get familiar with and understand a language's
idioms while implementing something I know well.

Personally, my two favourites are a puzzle called 5x5
([here](https://github.com/davep/5x5.xml),
[here](https://github.com/davep/Chrome-5x5),
[here](https://github.com/davep/5x5-for-Chrome),
[here](https://github.com/davep/5x5-Palm),
[here](https://github.com/davep/5x5.el),
[here](https://github.com/davep/5x5-react) and
[here](http://davep.org/misc/5x5/)), and writing a library or even a full
application to read [Norton Guide database
files](https://en.wikipedia.org/wiki/Norton_Guides)
([here](https://github.com/davep/ng2html),
[here](https://github.com/davep/w3ng),
[here](https://github.com/davep/eg-OS2),
[here](https://github.com/davep/weg1013),
[here](https://github.com/davep/weg), [here](https://github.com/davep/eg),
[here](https://github.com/davep/eg.el) and
[here](https://github.com/davep/jsNG)). Both are fun to work on, have
practical uses, and both have the benefit of being solved problems (for me)
that let me concentrate on the "how do I do *X* in this
language/toolkit/environment/framework/etc?".

Even with those two as my goto projects, I'm always open to new small
problems that might be fun to apply to languages I do know, or languages I
want to get to know (internally at work [we have a fun "league" of sorts,
writing a particular hamming distance calculation tool in different
languages](https://twitter.com/davepdotorg/status/1123952281156751361), for
example).

A few days ago, via [this repo on
GitHub](https://github.com/Lethrir/Journeys), I discovered [this fun little
problem](https://github.com/mikehadlow/Journeys). Right away I could see the
benefit in it. As a "go away and code up a solution" interview question it
strikes me as near-perfect. It's obviously not hard to solve, but it touches
on some basic but important aspects of software development and so will
allow the developer to show off how they approach things.

There's so many different approaches to it too. Even in a single language, I
could imagine having some fun writing the smallest code to solve the
problem, the most idiomatic code to solve the problem, the most supportable
and well-documented code to solve the problem, etc. And then there's the
thing I talk about above: knowing the solution and knowing it's easy, you
can then use it to learn the idiomatic way of solving the problem in new
languages.

Even better, [the README of the original repo links to solutions others have
written](https://github.com/mikehadlow/Journeys#other-solutions). Knowing
the problem, and knowing the solution, you can then go and read other
people's code and learn something about different styles and different
languages.

Over the next few weeks, as I get free time, I think I might just do this.
Take the "Journeys" problem and write versions in different languages I work
with, or know, and also use it to get to know languages I've yet to know or
use heavily (I'm especially keen to try a version in
[Julia](https://julialang.org/) -- a language I really like the look of and
want to find a reason to use).

Meanwhile, yesterday, I had a quick go at a first version in Python (aimed
at Python 3.8 or higher):
[https://github.com/davep/journeys.py](https://github.com/davep/journeys.py)

I set out to try and write something that was fairly idiomatic Python, which
uses tools that I tend to employ when working on Python projects (pipenv,
make, etc), and which also [used something I've never quite found a need for
so far](https://docs.python.org/3/library/dataclasses.html) in my usual
coding, but which I can see being useful and helpful.

I even threw in a couple of uses of [PEP
572](https://www.python.org/dev/peps/pep-0572/)!

I can see me tinkering with this some more over the next few days. I can
even see me writing a very different implementation in Python, just for the
fun of it.

I think that's what I like about this little problem. It's a good way to do
a bit of programming exercise; it's like the perfect way to do the
programming equivalent of going for a short run.

[//]: # (2019-11-10-going-on-a-journey.md ends here)
