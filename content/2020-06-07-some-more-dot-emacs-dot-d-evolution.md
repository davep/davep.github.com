---
layout: post
title: "Some more ~/.emacs.d evolution"
categories: []
tags: [ "emacs", "lisp" ]
date: 2020-06-07 16:48:00+0100
---

When I started with this version of the blog on Hashnode[^1], my plan was to
try and write something at least once a week. I managed to do that as far as
January this year, give or take, but then things got a little busy, the
world got trickier, and... Well, [you don't need me to tell you about
that](https://en.wikipedia.org/wiki/COVID-19_pandemic). Anyway, I'm back to
write some more and, hopefully, try and keep up with writing. I feel it'll
do me good.

I have been busy since January. Work has, as far as possible, carried on as
normal. The only big difference being I'm back working from home. It's an
odd turn of events personally given that I'd worked from home for 21 years,
then (with some trepidation) [went back to working in an
office](/2017/12/12/on_to_something_new.html). Having got used to being in
an office and being around people, it took some adjusting to working alone
again.

So, on to the main point of this post... During that period I've spent a lot
more time at my machine than I would normally, and so it was inevitable that
I'd end up tinkering with [my Emacs
configuration](https://github.com/davep/.emacs.d). While it's true that
[there's hardly a week goes by where I don't tinker with some small
thing](/2019/11/23/visual-evolution-of-emacs-config.html), I try not to make
huge changes too often. Huge changes do happen though.

A handful of weeks back was another one of those times where I made a big
change.

After I [burnt my original `~/.emacs` file back in
2016](/2016/05/26/starting_fresh_with_gnu_emacs.html) I've had an approach
where I've tried to make things as modular as possible, and as easy to clone
down to a new machine as possible. The design I came up with, [especially
once I moved over to using
`use-package`](/2017/07/13/more_revamping_of_my_emacs_config.html), has
served me well. But there was always one thing that bothered me: the files
that handled the loading and configuration of packages were, in effect,
[still three large monolithic
files](https://github.com/davep/.emacs.d/tree/728e74376bf5606d9ef2d297e36cc2d35e159d64/init.d/packages).
While this was better than a single monolithic `~/.emacs`, it still didn't
feel quite right.

Giving it a bit of thought, I decided that what I really wanted was a single
directory in which I could drop lots of small `.el` files that would handle
the loading and configuration of all sorts of packages. While it didn't gain
anything concrete, the idea felt tidier. Tidy is good. Feeling like the code
smell is good, is good too.

First though I needed a way to load multiple files, ideally within a whole
directory hierarchy, without needing to know in advance what files would be
there. After a little bit of tinkering I settled on [this bit of
code](https://github.com/davep/.emacs.d/blob/c3d53152b1adc9ba5e43baddb986870b3244b113/init.d/init-packages.el#L42-L46)
that revolves around the use of
[`directory-files-recursively`](https://www.gnu.org/software/emacs/manual/html_node/elisp/Contents-of-Directories.html):

```elisp
(let ((source (expand-file-name "init.d/packages.d/" user-emacs-directory)))
  (when (file-exists-p source)
    (cl-loop for use in (directory-files-recursively source (rx ".el" eol))
             do (load (file-name-sans-extension use)))))
```

Simply put, this code finds every file in and below
[`~/.emacs.d/init.d/packages.d/`](https://github.com/davep/.emacs.d/tree/master/init.d/packages.d)
whose name ends in `.el` (note the use of a regular expression, using
[`rx`](/2019/12/01/being-phony-and-lispy-regular-expressions.html)
to create it), removes the extension from the name, and loads it with `load`
(dropping the extension means `load` can decide if it wants to load the
compiled version of the code, or the source, depending on what's available).

After writing that I could then start to populate
`~/.emacs.d/init.d/packages.d/` with lots of smaller files that handled the
loading of packages. In some cases there's a file just for one package, in
other cases there's a file that handles a logical grouping of packages
(where there are obvious direct dependencies, or where one package is
designed to extend the other, etc). For now I've decided to break things
down into three directories that map to the three monolithic files I had
before:

![Screenshot 2020-06-07 at 16.36.28.png](/attachments/2020/06/07/Screenshot 2020-06-07 at 16.36.28.png)

However, I'm not totally wedded to this design and I may change this as time
goes on.

While I've not spent any time properly testing it out, I've also not really
noticed any obvious impact on startup speed. However, this tends not to be a
real concern for me. I seldom *start* Emacs anyway. I always have it running
[and use `emacsclient` as my editor in most places so files open instantly
in the running version of Emacs](https://github.com/davep/e).

[^1]: Note from future me: we're now back over on `blog.davep.org` of
    course.

[//]: # (2020-06-07-some-more-dot-emacs-dot-d-evolution.md ends here)
