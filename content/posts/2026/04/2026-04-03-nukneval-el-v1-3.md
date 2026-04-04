---
title: nukneval.el v1.3
date: 2026-04-03 15:09:19+0100
category: Emacs
tags: Emacs, Emacs Lisp, Lisp, coding, nukneval.el
---

Back when I first really got into writing [Emacs Lisp](/tag/emacs-lisp/)
code, one of the first things I got *very* used to and really fell in love
with was being able to
[`eval-last-sexp`](https://www.gnu.org/software/emacs/manual/html_node/emacs/Lisp-Eval.html)
(<kbd>C-x</kbd> <kbd>C-e</kbd>) the code I was writing, either to test it
right there in the buffer, or to cause it to be bound so I could use it
elsewhere. It was so different from any other mode of working I'd used
before and it was really addictive as a way of hacking on code.

Also quite quickly I got used to the fact that `eval-last-sexp` wasn't so
helpful with things like a `defvar` or a `defconst`, if I was changing them
up to try out new ways of doing things with the code I was working on; there
I had to remember to get used to using `eval-defun` (<kbd>C-M-x</kbd>).
Hardly a great problem, but something to keep in mind[^1].

Pretty quickly, as I worked on longer packages, I found myself wanting to,
in effect, unload a whole buffer of code and evaluate it again. From this
desire came [`nukneval.el`](https://github.com/davep/nukneval.el).

The original version of this has been sat around since 2002 or so, perhaps a
little earlier, and has served me well every time I've been messing with a
new package. While I suspect there is (now, perhaps was then too?) a better
way of doing things, the approach used in nukneval helped me learn some
things and served me well (and still does). Now it's muscle-memory to run
it.

The way it works is quite simple: go to the start of a buffer, `read` each
form, check if the `car` is of a given list of symbols, decide if it's
something I want to unbind, and then pick either `makunbound` or
`fmakunbound` and use that on the symbol. Finally, once the end of the
buffer has been hit: `eval-buffer`.

I've just released v1.3 as part of my slow wander through my old Emacs Lisp
packages, with this release cleaning up a deprecated use of `setf` to move
`point`, and also rewriting the code so it's a bit cleaner and also gives
better feedback.

[^1]: [Bozhidar Batsov](https://emacsredux.com/about/) recently wrote a good
    post [covering these sorts of
    issues](https://emacsredux.com/blog/2026/03/25/reloading-emacs-lisp-code/).

[//]: # (2026-04-03-nukneval-el-v1-3.md ends here)
