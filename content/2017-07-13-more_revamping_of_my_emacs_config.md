---
layout: post
title: More revamping of my Emacs config
categories: []
tags: Emacs, Lisp, programming, Emacs Lisp
date: 2017-07-13 15:25:29+0100
---

I've been pretty quiet on here since I last wrote about how I'd done a
further revamp of my Emacs config, so I thought that subject would be a good
reason to write another blog post.

It'll be a mostly short one, and one to muse over something that's been
bugging me for a while now: my decision to lean heavily on `customize` to
set all sorts of settings.

Initially,
[when I nuked my original config over a year ago](/2016/05/26/starting_fresh_with_gnu_emacs.html),
it seemed to make a lot of sense. Let all the tweaks and set values "hide"
in a file of their own and try and keep the hand-edited config files as
small and as clean as possible. Recently though I've got to thinking that
this obscures too much, hides too much detail, and removes the ability to
actually document what I'm doing and why. It also does make it tricky to
adapt some settings to different platforms or even environments on a single
platform.

Another problem I've run into is
this:
[when I made the second round of changes](/2017/04/01/another_revamp_of_my_emacs_config.html) and
decided to lean heavily
on [`use-package`](https://github.com/jwiegley/use-package), I soon ran into
the minor issue of some packages not making sense, or even being needed, on
some platforms (stuff that's useful on my macOS machines isn't always useful
on my Windows machines, that sort of thing). While `use-package` can handle
this easily thanks to the `:if` keyword, I'm still left with the fact that
`package-selected-packages` still gets populated.

Having `package-selected-packages` contain a list of installed packages
likely makes sense if you're using just the Emacs package system and you're
not doing the installing with `use-package` and `:ensure`. But with
`use-package` and `:ensure` I feel like I've got far more control over
things and can adapt what gets installed when depending on which Emacs I'm
running where.

But, because I'm syncing my `~/.emacs.d/.custom.el` to all my machines too, any
`use-package` that has a `:if` to not bother using a package has little
effect because the package still ends up being listed/loaded/seen as part of
the installation.

Ideally, I think, I'd like to be able to have `package-selected-packages`
held in its own file, or I'd only ever use `~/.emacs.d/.custom.el` for local
stuff (and so stop syncing it).

Starting today I'm going about a process of moving as much as I can out of
`~/.emacs.d/.custom.el` and into hand-edited files. In some respects I guess
I am going back to how I used to manage Emacs configuration, but this time
it's not a massive monolithic file-of-Lisp, it's neatly broken down into
sensible sections and it's also biased towards a "grab and config this
package" approach.

Meanwhile, I've not seen any good discussions online about `customize` vs
"hand-edit", which strikes me as a little odd as it feels like the perfect
"religious issue" for people to have endless disagreements over. I guess,
over the next couple or so weeks, I'll find out if switching back was a good
idea.

[//]: # (2017-07-13-more_revamping_of_my_emacs_config.md ends here)
