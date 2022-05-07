---
layout: post
title: "Why I really like fish abbreviations"
categories: []
tags: [ "TIL", "fish", "shell" ]
date: 2019-10-23 00:18:00+0100
---

*I'm filing this as a TIL because, while it wasn't T, I did L it very
recently and it was a new trick that impacted on around 25 years if prior
working practice.*

I think it must have been around 1991 when I first encountered
[4DOS](https://en.wikipedia.org/wiki/4DOS). While I'd used the odd Unix
shell here and there previously, it'd only been in passing. It was 4DOS that
first introduced me to the power of aliases on the command line. Many of the
aliases I set up and used in 4DOS still remain with me to this day, on
GNU/Linux and macOS, in some form or another.

I'm sure I don't need to tell anyone reading this why aliases and cool and
handy and pretty much vital if you do lots of work on the command line.

And then, a couple or so weeks ago, as a very recent convert to
[fish](https://fishshell.com/), I discovered the
[`abbr`](https://fishshell.com/docs/current/commands.html#abbr) command. At
first glance it didn't seem to make much sense. It was like
[`alias`](https://fishshell.com/docs/current/commands.html#alias), only it
expanded what you typed rather than acted as a command in its own right.

I did a bit of digging and some of it started to make sense. One thing that
really won me over -- and while it's something that doesn't directly impact
on me -- was the argument that it allows for a far more transparent command
history; especially if you're likely to use a transcript of a shell session
in a place where people might not know or have access to your aliases.

Imagine being in a position where you have loads of handy and cool aliases,
but you also need to record what you've done so other people can follow your
work (does it show that I sit amongst people who maintain lab notebooks?);
it seems like it would be a bit of a bother needing to record all of the
aliases in your own work environment up front. Without that information few
people will be able to make sense of the recorded commands, with that
information they'd still need to double-check what each command does.

So imagine an alias that, when used, expands in place. Then you'd get all of
the benefit of aliases while also having a full and readable record of what
you *actually* did.

Seems neat!

Here's a silly example. For a long time I've carried around an alias called
`greedy` that runs something like this:

```sh
du -hs * | sort -rh
```

It's pretty straightforward: I'm using `du` to get a sense of which
directories are using what space, and then using `sort` to make a
worst-to-best-offender list out of it. So I could use an alias:

```sh
alias greedy="du -hs * | sort -rh"
```

The only downside to this is that, any time I run it, if I were to record
the shell session and make it available for someone else to read, they'd
just see:

```sh
~/develop$ greedy
1.1G	JavaScript
824M	C
699M	rust
 93M	python
 33M	fonts
 33M	elisp
3.4M	zsh
3.0M	misc
1.1M	bash
840K	ocaml
428K	C++
316K	lisp
172K	Swift
152K	git
132K	ruby
 28K	ObjC
```

Now, with an abbreviation rather than an alias, I'd type `greedy` but as
soon as I hit `Enter` it'd get expanded to something anyone could read and
follow:

```sh
~/develop$ du -hs * | sort -rh
1.1G	JavaScript
824M	C
699M	rust
 93M	python
 33M	fonts
 33M	elisp
3.4M	zsh
3.0M	misc
1.1M	bash
840K	ocaml
428K	C++
316K	lisp
172K	Swift
152K	git
132K	ruby
 28K	ObjC
```

This is far from the only benefit of abbreviations; for most people it
probably isn't one of the most important ones, but I find it neat and
compelling and this alone drove me to rework almost all of my aliases as
abbreviations.

Having done that, I get other benefits too. For example, fish (like other
shells) has good support for argument completion for well-known commands.
The problem is, if you alias such a command, you don't get that completion.
With an abbreviation though you do! All you need to do is type the
abbreviation, hit `space` and it'll expand to the underlying command and
then the full range of completion can happen.

There's also one last reason why I like abbreviations over aliases, and it's
kind of a silly one, but in a good way. It's actually fun to see what you
type magically expand as you do things, it makes you look like you can type
even faster than you normally can! ;-)

PS: If you've never tried `fish` before and you're curious, it's easy to
[try in your browser](https://rootnroll.com/d/fish-shell/).

[//]: # (2019-10-23-why-i-really-like-fish-abbreviations.md ends here)
