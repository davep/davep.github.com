---
layout: post
title: Visual evolution of ~/.emacs.d
categories: []
tags: Emacs, Lisp, Emacs Lisp
date: 2019-11-23 14:42:00+0000
---

As detailed in a blog post I wrote [back in
2016](/2016/05/26/starting_fresh_with_gnu_emacs.html), I first got into
using Emacs in the mid 1990s, starting with it on OS/2 and then moving over
to GNU/Linux. It's been my often-used and much-loved development environment
for most of those years (I even have a couple of packages that are part of
Emacs itself).

For most of that time my configuration was a single `~/.emacs` file, which
was around 1,000 lines in length (including comments and whitespace). It'd
grown over the years, having special configuration sections for versions of
Emacs I didn't use any more, and operating systems I didn't work on any more
(yes, really, there were things in there specific to MS-DOS, for example).
On top of that I always hand-installed packages I used -- Emacs' package
management system having turned up long after I first got into using Emacs.

Then, in early 2016, I decided to nuke the whole thing and start from
scratch. As mentioned above, the start of this [is detailed in an older
post](/2016/05/26/starting_fresh_with_gnu_emacs.html). Another big round of
changes [happened round a year
later](/2017/04/01/another_revamp_of_my_emacs_config.html) -- which included
the birth of [delpa](http://blog.davep.org/delpa/) to manage my personal
packages. A couple or so months later there was [one last big round of
changes](/2017/07/13/more_revamping_of_my_emacs_config.html), mostly killing
off my enthusiastic embracing of
[`customize`](https://www.gnu.org/software/emacs/manual/html_node/emacs/Easy-Customization.html#Easy-Customization)
and instead going back to hand-set settings, only this time done via
[`use-package`](https://github.com/jwiegley/use-package).

The full history of this [can be found over on
GitHub](https://github.com/davep/.emacs.d), starting with the first "throw
everything away and start again" process and all the steps between then and
where my Emacs configuration is now.

Which brings me to the fun part of this blog post. Earlier this week I
stumbled on [Gource](https://gource.io/). It's a tool that's primarily
designed to visualise changes in repositories, although it can be used to
visualise anything that has a tree structure and changes over time (this
week I produced a video of the growth of my employer's electronic lab
notebook by hooking up the [Benchling](https://www.benchling.com/) API with
Gource, for example). So I got curious. What did it look like as I reworked
and tweaked and changed and tinkered with my Emacs configuration?

This is what it looked like:

[![](https://img.youtube.com/vi/bH4G80aZgsM/0.jpg)](https://www.youtube.com/watch?v=bH4G80aZgsM)

[//]: # (2019-11-23-visual-evolution-of-emacs-config.md ends here)
