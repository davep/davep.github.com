---
layout: post
title: I must be getting old
category: Emacs
tags: Emacs, Lisp, Emacs Lisp
date: 2022-08-23 21:31:00 +0100
---

A little earlier this evening I got [a new
issue](https://github.com/davep/boxquote.el/issues/7) raised against
[`boxquote.el`](https://github.com/davep/boxquote.el/issues/7). Apparently
Emacs 29 (I'm running 28.1 as of the time of writing) is moaning about the
likes of:

```elisp
(setf (point) some-location-or-other)
```

and

```elisp
(setf (buffer-string) "")
```

There's a whole background to why I've tended to code like that, that stems
from enjoying Common Lisp, my days reading (and sometimes posting to)
`comp.lang.lisp`, and I *think* some of the stuff [Erik
Naggum](https://en.wikipedia.org/wiki/Erik_Naggum) wrote back in the day. I
won't get into it all now; I'm not sure I can even remember a lot of how I
got there given how far back it was.

But...

Wanting to quickly get to the bottom of why the above was suddenly an issue,
I dived into the `NEWS` file and [found the
following](https://github.com/emacs-mirror/emacs/blob/67a15ce1564ce35ece24a19f00e03a36e0575746/etc/NEWS#L2585):

```
** Many seldom-used generalized variables have been made obsolete.
Emacs has a number of rather obscure generalized variables defined,
that, for instance, allowed you to say things like:

   (setf (point-min) 4)

These never caught on and have been made obsolete.  The form above,
for instance, is the same as saying

   (narrow-to-region 4 (point-max))

The following generalized variables have been made obsolete:
'buffer-file-name', 'buffer-local-value', 'buffer-modified-p',
'buffer-name', 'buffer-string', 'buffer-substring', 'current-buffer',
'current-column', 'current-global-map', 'current-input-mode',
'current-local-map', 'current-window-configuration',
'default-file-modes', 'documentation-property', 'frame-height',
'frame-visible-p', 'global-key-binding', 'local-key-binding', 'mark',
'mark-marker', 'marker-position', 'mouse-position', 'point',
'point-marker', 'point-max', 'point-min', 'read-mouse-position',
'screen-height', 'screen-width', 'selected-frame', 'selected-screen',
'selected-window', 'standard-case-table', 'syntax-table',
'visited-file-modtime', 'window-height', 'window-width', and
'x-get-secondary-selection'.
```

As suggested above... this is my thing, this is how I coded some Elisp
stuff. Look through much of my [Emacs Lisp code](https://elisp.dev/) and
you'll find me `setf`ing stuff all over the place.

Apparently my style is "obscure". Actually, I'm kinda okay with that if I'm
honest.

This is going to be a bit of a pain in the arse; I'm going to have to go
through a whole bunch of code and make it "less obscure", at some point.

But...

This isn't the part that had me thinking I must be getting old. Oh no. The
`NEWS` file had another little surprise in store:

```
** The quickurl.el library is now obsolete.
Use 'abbrev', 'skeleton' or 'tempo' instead.
```

That.... that's me that is. Well, it's one of the me things. If you run
`about-emacs`, dive into `Authors`, and search for my name, in any copy of
GNU Emacs from the last decade or two, you'll find this:

```
Dave Pearson: wrote 5x5.el quickurl.el
```

[`quickurl.el`](https://github.com/davep/quickurl.el/blob/master/quickurl.el)
was a package I wrote back in the late 1990s, back when I was a very heavy
user of [Usenet](https://en.wikipedia.org/wiki/Usenet), and often found
myself posting the same URLs in posts again and again; especially in
`comp.lang.clipper`. As a fairly quick hack I wrote the code so that I could
very quickly insert often-used URLs.

Some time later, I got an email from the
[FSF](https://en.wikipedia.org/wiki/Free_Software_Foundation) (I actually
think it was from [RMS](https://en.wikipedia.org/wiki/Richard_Stallman) --
but that's an [`mbox`](https://en.wikipedia.org/wiki/Mbox) I've long ago
lost -- or a backup of it might be in storage back in England, on a DVD),
asking if I wanted to contribute it to Emacs proper. This seemed like an odd
thing to add to Emacs but, sure, why the hell not?

And so I had my second contribution to a body of code I used a lot (the
first being [`5x5.el`](https://github.com/davep/5x5.el) -- which itself was
my first ever attempt at writing some non-trivial Elisp code).

So... yeah... here we are. I'm now old enough to have written some Emacs
Lisp code, had it required by the FSF for inclusion in Emacs, had it live in
there for something like two decades, and then *become obselete*!

[//]: # (2022-08-23-I-must-be-getting-old.md ends here)
