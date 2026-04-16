---
title: boxquote.el v2.4
date: 2026-04-16 08:29:35+0100
category: Emacs
tags: Emacs, Emacs Lisp, Lisp, coding, boxquote.el
cover: /attachments/2026/04/16/boxquote.png
---

[`boxquote.el`](https://github.com/davep/boxquote.el) is another of my
oldest [Emacs Lisp](/tag/emacs-lisp/) packages. The original code itself was
inspired by something I saw on Usenet, and writing my own version of it
seemed like a great learning exercise; as noted in the thanks section in the
commentary in the source:

> Kai Grossjohann for inspiring the idea of boxquote. I wrote this code to
> mimic the "inclusion quoting" style in his Usenet posts. I could have
> hassled him for his code but it was far more fun to write it myself.

While I never used this package to quote text I was replying to in Usenet
posts, I did use it a *lot* on Usenet, and in mailing lists, and similar
places, to quote *stuff*.

The default use is to quote a body of text; often a paragraph, or a region,
or perhaps even Emacs' idea of a `defun`.

```
,----
| `boxquote.el` provides a set of functions for using a text quoting style
| that partially boxes in the left hand side of an area of text, such a
| marking style might be used to show externally included text or example
| code.
`----
```

Where the package really turned into something fun and enduring, for me, was
when I started to add the commands that grabbed information from elsewhere
in Emacs and added a title to explain the content of the quote. For example,
using `boxquote-describe-function` to quote the documentation for a function
at someone, while also showing them how to get at that documentation:

```
,----[ C-h f boxquote-text RET ]
| boxquote-text is an autoloaded interactive native-comp-function in
| ‘boxquote.el’.
|
| (boxquote-text TEXT)
|
| Insert TEXT, boxquoted.
`----
```

Or perhaps getting help with a particular key combination:

```
,----[ C-h k C-c b ]
| C-c b runs the command boxquote (found in global-map), which is an
| interactive native-comp-function in ‘boxquote.el’.
|
| It is bound to C-c b.
|
| (boxquote)
|
| Show a transient for boxquote commands.
|
|   This function is for interactive use only.
|
| [back]
`----
```

Or figuring out where a particular command is and how to get at it:

```
,----[ C-h w fill-paragraph RET ]
| fill-paragraph is on fill-paragraph (M-q)
`----
```

While I seldom have use for this package these days (mainly because I don't
write on Usenet or in mailing lists any more) I did keep carrying it around
(always pulling it down [from melpa](https://melpa.org/#/boxquote)) and had
all the various commands bound to some key combination.

```elisp
(use-package boxquote
  :ensure t
  :bind
  ("<f12> b i"   . boxquote-insert-file)
  ("<f12> b M-w" . boxquote-kill-ring-save)
  ("<f12> b y"   . boxquote-yank)
  ("<f12> b b"   . boxquote-region)
  ("<f12> b t"   . boxquote-title)
  ("<f12> b h f" . boxquote-describe-function)
  ("<f12> b h v" . boxquote-describe-variable)
  ("<f12> b h k" . boxquote-describe-key)
  ("<f12> b h w" . boxquote-where-is)
  ("<f12> b !"   . boxquote-shell-command))
```

Recently, with the [creation of `blogmore.el`](/tag/blogmore-el/), I moved
the boxquote commands off the <kbd>b</kbd> prefix (because I wanted that for
blogging) and onto an <kbd>x</kbd> prefix. Even then... that's a lot of
commands bound to a lot of keys that I almost never use but still can't let
go of.

Then I got to thinking: [I'd made good use of transient in
`blogmore.el`](/2026/04/04/blogmore-el-v2-6.html), why not use it here too?
So now `boxquote.el` has acquired a `boxquote` command which uses transient.

![The boxquote transient in action](/attachments/2026/04/16/boxquote.png#centre)

Now I can have:

```elisp
(use-package boxquote
  :ensure t
  :bind
  ("C-c b" . boxquote))
```

and all the commands are still easy to get to and easy to (re)discover. I've
also done my best to make them context-sensitive too, so only applicable
commands should be usable at any given time.

[//]: # (2026-04-16-boxquote-el-v2-4.md ends here)
