---
layout: post
title: "Starting fresh with GNU emacs"
categories: []
tags: [emacs]
published: True
date: 2016-05-26 12:28:48+0100
---

As I've mentioned elsewhere on this blog, over the past few years, my
use of GNU emacs has lapsed somewhat. There was a time when it was my
only editor (except for the odd dips into vim to do some quick
editing) and, back when I used to use GNU Linux as a desktop machine a
lot, I'd have an emacs session up and running pretty much non-stop (it
was one of the reasons I wrote
[uptimes.el](https://github.com/davep/uptimes.el)).

In more recent times I've been working more on Windows and often
inside Visual Studio. Even for my own "for fun" programming, I've
mostly being doing things that didn't involve emacs much. In fact,
most of my recent "for fun" coding has been done using
[Sublime Text](https://www.sublimetext.com/) because it was powerful,
cross-platform and also had great support for
[the language I code in a lot when it comes to personal amusement projects](http://wiki.secondlife.com/wiki/LSL_Portal).

During that time I've wanted to get back into emacs. Quite a bit seems
to have changed since I was last a very avid user and this also meant
wanting and needing to catch up.

The first thing I needed to do was finally get around to killing off
my old `~/.emacs` file. This has followed me around since I first got
into emacs on OS/2 back in the mid 1990s. The file started out with a
few `setq` expressions to tweak some settings and just kept growing
and growing. It'd got to a point where there was old stuff in there
that I had no use for and sometimes even no idea what it was
for. Heck, to give some idea of how old the file was: there were items
in there that handled running emacs on MS-DOS!

So, a couple of weeks back, I dumped it. Dumped the whole lot. The
plan then was to recreate it with as little hands-on coding as
possible. I decided that, as much as I could, I'd tweak using
`customize` and only hand-code (in `~/.emacs.d/init.el` this time
around) things when there was no obvious other way to do it.

So far this is working out really well. Gone has the ugly and
monolithic `.emacs`, replaced with something far more modular, much
more tidy and far easier to maintain. Whereas my old config was almost
1,000 lines long, the new `init.el` is currently just 50 lines:

```elisp
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Make use of the Common Lisp compatibility module.
(require 'cl)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Local config/lib directory support.

(defun davep:user-path (path)
  "Given `file', return a path for it in the local config."
  (concat user-emacs-directory path))

(defvar davep:local (davep:user-path "davep/")
  "My local config and code directory.")

(defvar davep:startup (davep:user-path "davep/startup")
  "My local startup code.")

(defvar davep:lib (davep:user-path "davep/lib")
  "My local library code.")

(defvar davep:lib-3rd-party (davep:user-path "davep/lib-3rd-party")
  "My local third party code.")

(push davep:local         load-path)
(push davep:startup       load-path)
(push davep:lib           load-path)
(push davep:lib-3rd-party load-path)

(defun have-own-package-p (package)
  "Does a package of my own exist in this environment?"
  (locate-library package nil (list davep:lib)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Ensure custom values go in their own file.
(setq custom-file (davep:user-path "custom.el"))
(load custom-file)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Load various startup things.
(load "env-tests")
(require 'davep-keys)
(require 'davep-languages)
(require 'davep-style)
(require 'uptimes)
(require 'csrclr)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Local autoloading.
(require 'autoloading)
(load-davep-autoloads)
```

All the other stuff, things to tweak language modes so they intend
"just so", my own special keyboard bindings, that sort of thing,
they're all farmed off into their own files:

```shell
davep@Bellerophon:~/.emacs.d/davep/startup$ v
total 40
-rw-r--r--  1 davep  staff  4211 24 May 14:38 davep-keys.el
-rw-r--r--  1 davep  staff  4078 16 May 13:51 davep-languages.el
-rw-r--r--  1 davep  staff   537 25 May 14:13 davep-style.el
-rw-r--r--  1 davep  staff  1339 16 May 09:39 env-tests.el
```

Another thing I'm trying to do is dump all the old third party code I
had locally and, instead, use emacs' own package manager
now. Currently this is also working well for me given that I'm using
both [ELPA](https://elpa.gnu.org/) and [MELPA](https://melpa.org/#/).

I haven't managed to dump everything yet, but it's a useful exercise
to slowly work through the various files I was carting around and
deciding if I need them or not (like, I'm fairly sure I won't be
needing a `cobol-mode` any time soon -- that can go).

On top of all of this, on top of starting with a "clean slate" emacs,
I've also started keeping track of what I do on GitHub. I've got a
private repo for my `~/.emacs.d/` that I can now easily sync between
my various machines.

One final thing that I'm starting to try and do is actually make full
use of emacs again. One example is that I'm writing this blog post in
it. Until now I've been using SublimeText with
[a Jekyll package to compose and manage things](https://packagecontrol.io/packages/Jekyll)
but, this time around I'm giving [hyde](https://melpa.org/#/hyde) and
[markdown-mode](https://melpa.org/#/markdown-mode) a go. So far
they're working out pretty well too (albeit hyde was a bit odd to set
up and isn't 100% making sense to me yet).
