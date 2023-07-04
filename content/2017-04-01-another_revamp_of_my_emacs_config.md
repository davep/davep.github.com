---
layout: post
title: "Another revamp of my emacs config"
categories: []
tags: [emacs, lisp, programming]
date: 2017-04-01 10:02:18+0100
---

Just under a year ago I decided to
[totally rewrite my GNU emacs config](/2016/05/26/starting_fresh_with_gnu_emacs.html).
As I wrote at the time, it'd been following me around all sorts of machines
since the early 1990s, starting life on an OS/2 Warp machine and travelling
via MS-DOS, GNU/Linux, Windows and, these days, macOS.

The changes I made last year have served me really well, but there were two
related issues with it that bothered me a little: the fact that I was
maintaining a local library of elisp code in the repository and, worse
still, I was storing the packages I'd installed from elpa and melpa in the
repository as well.

While this did mean it was pretty easy for me to start up a new installation
of emacs on a machine -- all I had to do was clone the repo and run up emacs
-- I wasn't happy with the duplication involved. I didn't like holding code
in my `.emacs.d` repo that was already held in package archives.

The solution I saw was in two parts:

1. Get some of my code, that might be useful to others, into melpa.
2. Somehow sort my own package archive for my personal code.

<p></p>

Over the past week or so I've worked on this approach. It initially started
with me tackling item 1 above: I tidied up and
submitted
[`obfusurl.el`](https://github.com/davep/obfusurl.el),
[`protocols.el`](https://github.com/davep/protocols.el),
[`services.el`](https://github.com/davep/services.el),
[`thinks.el`](https://github.com/davep/thinks.el) and
[`uptimes.el`](https://github.com/davep/uptimes.el). This was a really
helpful process in that it allowed me to brush up on my elisp and emacs
knowledge. It's a good 15+ years since I last wrote any significant elisp
code and things have moved on a little in that time.

Having done that I'd managed to move a handful of my own packages out of my
local library of code, and so out of my `.emacs.d` repo, but it left me with
the problem of what to do with the rest of it.

That's when I discovered `package-x` and:

```
,----[ C-h f package-upload-buffer RET ]
| package-upload-buffer is an interactive compiled Lisp function in
| ‘package-x.el’.
|
| (package-upload-buffer)
|
| Upload the current buffer as a single-file Emacs Lisp package.
| If ‘package-archive-upload-base’ does not specify a valid upload
| destination, prompt for one.
`----
```

(plus `package-upload-file` too, of course). This meant I could, in effect,
start my own personal package archive and look at tackling issue 2 above.

This did give me one small problem though: how and where would I host the
archive? I did consider hosting it on a DigitalOcean droplet, but that felt
a little like overkill for something so simple. And then I
realised: [GitHub Pages](https://pages.github.com/)! All I needed to do was
keep the package archive in its own repo (which I would have done anyway)
and then make the whole repo the source for a GitHub Pages site. A quick
test later and... it worked!

So, by this point, I'd farmed some of my code off to melpa, and now had the
rest of it in "delpa" (which I'd called my personal archive). I could now
use the emacs package management system to install third party packages and
also my own.

But I was still left with one issue: I was still holding the installed
packages inside my `.emacs.d` repo by way of ensuring that all machines were
in sync in terms of what was installed. Now I needed to work out how to
solve that.

Around this time, as luck would have
it, [@tarsius](https://github.com/tarsius)
had
[suggested I look at](https://github.com/davep/boxquote.el/pull/1#issuecomment-288462491) a
package called [`use-package`](https://github.com/jwiegley/use-package)
by [@jwiegley](https://github.com/jwiegley). This was the bit I was missing.

With `use-package` I would be able to declare which packages I needed, how
they'd be installed and, most important of all, it could be set to handle
the fact that the package wasn't even installed. If a package is requested
and there is no local install `use-package` is smart enough to get the emacs
package system to install it.

So, given that, all I need to do was [create a startup file that would
declare the packages I use](https://github.com/davep/.emacs.d/blob/1fa67c2895f345098057654f6acb3b57a77f1194/startup/davep-packages.el) and
I'd have a setup that should, once I'd cloned `.emacs.d`, self-install.

Except... yeah, one more issue. `use-package` isn't part of GNU emacs yet so
I'd need a method of getting it to auto-install so it could then handle
everything else. As it was that was as easy as adding this to the start of
my [`init.el`](https://github.com/davep/.emacs.d/blob/master/init.el).

```elisp
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Make sure the package system is up and running early on.
(require 'package)
(add-to-list 'package-archives '("melpa" . "http://melpa.org/packages/"))
(add-to-list 'package-archives '("delpa" . "http://blog.davep.org/delpa/"))
(package-initialize)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Bootstrap `use-package'
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))
```

With that in place I was able to nuke all my config on a machine, clone a
fresh copy of `.emacs.d` (having now ceased tracking and storing the
installed packages in that repo), run up emacs, wait a few moments and then
find that everything was installed and ready to use.

Perfect!

My [`.emacs.d`](https://github.com/davep/.emacs.d) is now a lot smaller than
it was before and, I think, even easier to maintain. Right now I think I'm
very close to the ideal emacs config that I wanted to create when I did the
complete rewrite a year ago.

