---
layout: post
title: Being phony, and Lispy regular expressions
categories: []
tags: Emacs, Lisp, Emacs Lisp
date: 2019-12-01 16:42:00+0000
---

While it does seem that they're a little out of fashion these days, in some
circles anyway, I'm still an avid fan of `make` and make files. Even in
environments where I don't need a `Makefile` to actually build anything,
I'll use one (or more) to help create handy shortcuts for getting stuff
done.

Looking at the main `Makefile` for one of my major work projects, there's 45
targets that help fire off various jobs (all of them [self-documenting using
a variation on an approach I read a while
back](https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html)).

In most cases the targets aren't real targets. That's to say, they don't
build the thing they're called. They are [phony
targets](https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html).
So, as makes sense, I make a point of marking them all as such. I follow the
convention that has the `.PHONY` marker appear on the line before the
target; this feels cleaner to me and easier to follow and maintain.

But.... I'm lazy. And I use Emacs. Typing out `.PHONY foo` all the time
feels like far too much work. So, some time ago, I quickly threw together
[`make-phony.el`](https://github.com/davep/make-phony.el).

With this I could be *really* lazy. I could type out the `Makefile` target
and then, with my cursor on it, press a key combination and have the
`.PHONY` marker put in place.

Does it save much time? Yeah, probably not really. But it was a fun little
exercise and an excuse to write a little bit of Emacs Lisp.

There's one thing I made a point of doing in the heart of this too: using
`rx`. For anyone who doesn't know of it, think of it as a very Lispy way of
writing regular expressions. I won't even try and explain it all here
[because others have done an excellent job
already](http://francismurillo.github.io/2017-03-30-Exploring-Emacs-rx-Macro/).
What I will do is say this: if you're in the habit of writing some Emacs
Lisp, or even tinkering with your configuration, and you find yourself
writing a regular expression, consider looking at `rx` -- it's well worth
the time to get to know it.

Slowly, as time goes on, I'm weeding out "vanilla" regular expressions from
my config and code and moving over to using `rx`. I feel, quite rightly I
think, that [something like
this](https://github.com/davep/.emacs.d/blob/b3185a1dbaa0a16f540465844b84c5e1c6a77180/init.d/packages/init-packages-melpa.el#L117-L126):

```elisp
(rx
 (or
  ;; Ignore hidden files.
  (group bol ".")
  ;; I never want to edit the desktop.
  (group "Desktop/" eol)
  ;; Ignore compiled files.
  (group "." (or "pyc" "elc") eol)
  (group ".egg-info/" eol)))
```

is much easier to write, read and maintain, than this:

```
"\\(^\\.\\)\\|\\(Desktop/$\\)\\|\\(\\.\\(?:\\(?:\\(?:el\\|py\\)c\\)\\)$\\)\\|\\(\\.egg-info/$\\)"
```

I mean, even *if* the regular expression above can be written in a more
efficient way (and I imagine it can), as someone working in a Lisp
environment, I'd much sooner write and work with the `rx` version.

[//]: # (2019-12-01-being-phony-and-lispy-regular-expressions.md ends here)
