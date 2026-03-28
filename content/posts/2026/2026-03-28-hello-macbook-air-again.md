---
title: Hello MacBook Air (again)
date: 2026-03-28 10:30:09+0000
category: Tech
tags: Mac, Apple, macOS, MacBook, MacBook Air
cover: /attachments/2026/03/28/macbook-air.jpeg
---

As I [mentioned yesterday](/2026/03/27/macbook-air-m5.html) I decided it was
time to update my portable/sofa hacking setup and treat myself to a nice new
MacBook Air. It's here (well, I picked it up yesterday evening after
dinner).

![MacBook Air M5](/attachments/2026/03/28/macbook-air.jpeg#centre)

So far I'm *very* pleased with the choice. It's light but feels sturdy. The
screen is very pleasing to read. The keyboard is really nice to type on
(albeit I do prefer the old MacBook Pro, but on the other hand this is a bit
more quiet, which matters if you're sharing a living room with someone
else). It's fast. So fast! It's also so quiet! So very quiet! And cool too.
The Intel-based MacBook Pro would get very warm as I worked; this just stays
cold.

The really great part though is the battery life. Depending on what I was
doing, with the Intel Pro, I'd get a couple of hours off the cable. On the
other hand, last night, I spent a few hours setting things up on the Air and
I barely noticed the battery drop at all. This, more than anything, is what
I wanted.

Well, okay, I wanted the speed, the quiet, the lack of heat, and the long
battery life.

Oh, and the rather lovely "Midnight" colour. It's not black, but it's close
enough.

The setup itself went pretty well, although for some odd reason I ran into
problems when setting up Emacs. These days I always use [Emacs Plus via
Homebrew](https://github.com/d12frosted/homebrew-emacs-plus) and have never
had issues. Weirdly though, this time, if I did the installation method that
builds locally all sorts of things went wrong. I don't know if I missed a
step or something but I did what I normally do when dropping Emacs on a Mac.
So I started again with the pre-built approach and that worked better.

Even then though, I ran into problems with [my setup downloading
everything](https://github.com/davep/.emacs.d). Things *mostly* worked but I
kept seeing all sorts of issues relating to `git-gutter` and
`git-gutter-fringe` not being able to load (despite the fact they'd
downloaded fine, from what I could see).

In the end I gave up trying to get it to all work from scratch and
hand-removed and then hand-installed via `package-list-packages` instead.
Not the most scientific of approaches, and one I'm sure I'll regret at some
point in the future, but at least I got to a point where I could get other
stuff done on the machine.

All of which is to say: if you're reading this blog post I got my Emacs and
git environment to the point I can write things and push them out to the
world. At which point that's the really important stuff up and going and I
can call this "set up".

Once I'm happy that's working, I think it's time to revisit my Emacs setup.
While I don't think it needs another [complete
restart](/2016/05/26/starting_fresh_with_gnu_emacs.html), I think it might
be time to at least look through what I have loading in and perhaps remove
some things I don't use any more (for example, I always carry around `vterm`
from the days when I was testing every possible terminal I could get my
hands on -- [that's less important to me these
days](/2024/03/28/goodbye-textualize.html).)

[//]: # (2026-03-28-hello-macbook-air-again.md ends here)
