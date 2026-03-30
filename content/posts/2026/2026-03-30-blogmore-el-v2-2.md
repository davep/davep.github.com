---
title: blogmore.el v2.2
date: 2026-03-30 20:31:03+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, coding, defmacro
---

It really feels like [BlogMore](https://blogmore.davep.dev/) has kicked off
a whole new thing when it comes to personal hacking. During the past few
years I've developed a *lot* of [Python](/tag/python/) applications and
libraries, and have had a ton of fun doing so, but during that time I've not
really done anything with writing stuff for [Emacs](/tag/emacs/).

To a large degree I think this says something about how stable Emacs is for
me (I've been using it for a touch over 30 years at this point, you'd think
I'd be kind of settled with it), but it's still always fun to have a reason
to hack on some [Lisp](/tag/lisp/) code. There's little doubt my Lisp --
especially Emacs Lisp -- has got a wee bit rusty.

So I'm having a lot of fun at the moment falling into the rabbit hole of
expanding on and tinkering with
[`blogmore.el`](https://github.com/davep/blogmore.el). The reason I've just
made v2.2 is a good example of exactly this. There are no real user-facing
changes in the code, it was all things I just wanted to tidy up.

The main thing that has been bugging me for the past day is the repeating
boilerplate that resulted from adding all the different current-blog-aware
setting getter functions. There were 7 different functions, all looking like
this:

```elisp
(defun blogmore--post-maker-function ()
  "Get the post maker function for the current blog."
  (or
   (blogmore--blog-post-maker-function (blogmore--chosen-blog))
   blogmore-default-post-maker-function))
```

Exact same pattern, the only thing different being the name of the getter
function being called on, and the name of the variable that contained the
global default value.

So just a little earlier I cleaned this up using one of my favourite things
about Lisp: `defmacro`. There's something about macros that makes me really
like coding in Lisp, and which I cite as a *really good thing* when asked
why I like Lisp, but which I always seem to utterly fail to explain well.
Macros feel like one of those things you just have to experience for
yourself to really get[^1].

Now, thanks to this:

```elisp
(defmacro blogmore--setting (setting)
  "Generate a function to get the value of SETTING for the current blog."
  `(defun ,(intern (format "blogmore--%s" setting)) ()
     ,(format "Get the %s for the current blog." setting)
     (or (,(intern (format "blogmore--blog-%s" setting)) (blogmore--chosen-blog))
         ,(intern (format "blogmore-default-%s" setting)))))
```

all those 7 functions can collapse to this[^2]:

```elisp
(blogmore--setting post-template)
(blogmore--setting post-maker-function)
(blogmore--setting category-maker-function)
(blogmore--setting tag-maker-function)
(blogmore--setting post-link-format)
(blogmore--setting category-link-format)
(blogmore--setting tag-link-format)
```

Now the code is shorter, cleaner, and if I need to change anything I only
need to change it in one place. Sure, the latter part especially is one of
those *"you could do that with a function too"* things (have the work in one
place), but here I can get the language to write me a whole load of
functions, all of which refer to different functions and variables, each one
based off just the one symbol.

The point of all of this being: v2.2 of `blogmore.el` is now out, it adds
nothing for the user (who I suspect is only me anyway), but I had an
absolute blast dusting off more of my Emacs Lisp knowledge and getting back
the urge to code [even more Emacs Lisp](https://elisp.dev/).

All of this has even got me tidying up my `~/.emacs.d/` *and* has me
thinking I should go back through some of my older code and [clean up all
that legacy nonsense](/2022/08/23/i-must-be-getting-old.html).

[^1]: There was a time I would have said "grok" here but... well that's
    spoiled now.

[^2]: I suppose I could reduce that to one "call" with a loop over a list of
    symbols, but that feels unnecessary here.

[//]: # (2026-03-30-blogmore-el-v2-2.md ends here)
