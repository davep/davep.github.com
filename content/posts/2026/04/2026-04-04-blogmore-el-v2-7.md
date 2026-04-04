---
title: blogmore.el v2.7
date: 2026-04-04 19:24:39+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, blogmore.el, coding, transient
---

There's no question that the
[experiment](/2026/02/20/five-days-with-copilot.html) that is
[BlogMore](https://blogmore.davep.dev/) has resulted in me blogging more.
Although my previous setup wasn't exactly all friction, there's something
about "owning" most of the tools and really knowing how they work, and being
able to quickly modify them so they work "just so", that makes me more
inclined to quickly write something up.

I can see this if I look at the [numbers in the archive for this
blog](/archive/). In [March alone](/2026/03/) I wrote 43 posts; that's more
than I wrote in any whole year, other than [2023](/2023/). While I suspect
this will start to calm down as work on BlogMore and
[`blogmore.el`](https://github.com/davep/blogmore.el) settles down, I sense
I'll be writing a bit more often for some time to come.

Because of this I decided to do a little bit of housekeeping on the [posts
directory](https://github.com/davep/davep.github.com/tree/main/content/posts)
in the blog's [source
repository](https://github.com/davep/davep.github.com). Originally I had the
Markdown source for every post all in one directory. Then last month [I
broke those down by
year](https://github.com/davep/davep.github.com/pull/59). Then earlier
today, seeing how this year is going, [I decided to break 2026 down by
month](https://github.com/davep/davep.github.com/pull/137).

Then I realised I had a problem in `blogmore.el`. It assumed that the
Markdown file for a new post (`blogmore-new`) would always be created in a
subdirectory named after the year, underneath the defined posts directory.
Until today that was the case[^1], but now *I* wanted it to work
differently.

So this is why I'm making a second release in one day: [I added the ability
to configure the subdirectory where a new post is
created](https://github.com/davep/blogmore.el/pull/45). I've changed the
default now so that it assumes the user wants the subdirectory to be
`YYYY/MM/DD` (because more granular feels like the right default). In my
case I don't want that, I just want `YYYY/MM`, but now I can configure that.
The value that is set is a function that returns the name of the
subdirectory, so in the case of my blog I have it as:

```elisp
(lambda () (format-time-string "%Y/%m/"))
```

On the other hand, for my [photoblog](https://seen-by.davep.dev/) I want the
full date as a subdirectory so I can leave it as the default. The whole
`use-package` for `blogmore` now looks like:

```elisp
(use-package blogmore
  :ensure t
  :defer t
  :vc (:url "https://github.com/davep/blogmore.el" :rev :newest)
  :init
  (add-hook 'blogmore-new-post-hook #'end-it)
  (blogmore-work-on "blog.davep.org")
  :custom
  (blogmore-blogs
   '(("blog.davep.org"
      ;; Root directory for posts.
      "~/write/davep.github.com/content/posts/"
      ;; Subdirectory for new posts, relative to the root.
      (lambda () (format-time-string "%Y/%m/")))
     ("seen-by.davep.dev"
      ;; Root directory for posts.
      "~/write/seen-by/content/posts/")))
  :bind
  ("<f12> b" . blogmore))
```

Technically this is a breaking change because it bumps [the meaning of each
"position" in the values within
`blogmore-blogs`](https://github.com/davep/blogmore.el/blob/b80743391eedeb507c5b743c1af531701a2f858a/blogmore.el#L48-L86).
However, in my case, because I was only ever defining the blog name and the
top-level directory for the posts (both mandatory), this didn't break
anything; I also strongly suspect nobody else is using this so I very much
doubt I'm messing with someone else's setup[^2]. If I have I apologise; do
let me know.

Anyway, all of this goes to explain why the heck I made two releases of the
same package back to back in the same day. This is what happens when [my
namesake is having fun
outside](https://www.metoffice.gov.uk/about-us/news-and-media/media-centre/weather-and-climate-news/2026/amber-wind-warning-for-easter)
and so I just want to sit on the sofa, hack on some code, and watch the
chaos in the garden.

[^1]: For my blog, which again shows that `blogmore.el` started as a quick
    hack for getting work done on my blog, but I also want to make it as
    configurable as possible.

[^2]: Even if someone else *is* using this I would suspect they hadn't
    configured anything more than I have.

[//]: # (2026-04-04-blogmore-el-v2-7.md ends here)
