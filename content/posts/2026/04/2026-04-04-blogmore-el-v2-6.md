---
title: blogmore.el v2.6
date: 2026-04-04 11:48:21+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, blogmore.el, coding, transient
cover: /attachments/2026/04/04/transient-cover.png
---

Like most people, I imagine, I first ran into
[transient](https://www.gnu.org/software/emacs/manual/html_mono/transient.html)
when first using [magit](https://magit.vc/). I took to it pretty quickly and
it's always made sense to me as a user interface. But... I've never used it
for any code I've ever written.

I think, incorrectly, I'd half assumed it was going to be some faff to set
up, and of course for a good while it wasn't part of Emacs anyway. Given
this, I'd always had it filed under the heading *"that's so neat I'll give
it a go one day but not at the moment"*.

Meanwhile... ever since I did the last big revamp of my [Emacs
configuration](https://github.com/davep/.emacs.d), I found myself leaning
into a command binding approach that does the whole *prefix-letter-letter*
thing. For reasons I can't actually remember I fell into the habit of using
<kbd>F12</kbd>[^1] as my chosen prefix key. As such, over the past 10 or so
years (since I greatly overhauled my Emacs setup), I've got into setting up
bindings for commands that follow this prefix convention.

So when I created [`blogmore.el`](https://github.com/davep/blogmore.el) I
set up the commands following this pattern.

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
   '(("blog.davep.org" "~/write/davep.github.com/content/posts/")
     ("seen-by.davep.dev" "~/write/seen-by/content/posts/")))
  :bind
  ("<f12> b b" . blogmore-work-on)
  ("<f12> b n" . blogmore-new)
  ("<f12> b e" . blogmore-edit)
  ("<f12> b d" . blogmore-toggle-draft)
  ("<f12> b s c" . blogmore-set-category)
  ("<f12> b a t" . blogmore-add-tag)
  ("<f12> b u d" . blogmore-update-date)
  ("<f12> b u m" . blogmore-update-modified)
  ("<f12> b l p" . blogmore-link-post)
  ("<f12> b l c" . blogmore-link-category)
  ("<f12> b l t" . blogmore-link-tag))
```

It works well, it makes it nice and easy to remember the bindings, etc.
Nobody needs me to sell them on the merits of this approach.

Then I got to thinking last night: why am I setting up all those bindings
when I could probably do it all via a transient? So that was the moment to
actually RTFM and get it going. The first version was incredibly quick to
get up and running and I was kicking myself that I'd taken so long to
actually look at the package properly.

This morning I've worked on it a little more and the final form is still
pretty straightforward.

```elisp
(transient-define-prefix blogmore ()
  "Show a transient for BlogMore commands."
  [:description
   (lambda ()
     (format "BlogMore: %s\n"
             (if (blogmore--chosen-blog-sans-error)
                 (blogmore--blog-title)
               "No blog selected")))
   ["Blog"
    ("b"  "Select blog" blogmore-work-on)]
   ["Post"
    ("n" "New post" blogmore-new :inapt-if-not blogmore--chosen-blog-sans-error)
    ("e" "Edit post" blogmore-edit :inapt-if-not blogmore--chosen-blog-sans-error)
    ("d" "Toggle draft status" blogmore-toggle-draft :inapt-if-not blogmore--blog-post-p)
    ("c" "Set post category" blogmore-set-category :inapt-if-not blogmore--blog-post-p)
    ("t" "Add tag" blogmore-add-tag :inapt-if-not blogmore--blog-post-p)
    ("u d" "Update date" blogmore-update-date :inapt-if-not blogmore--blog-post-p)
    ("u m" "Update modified date" blogmore-update-modified :inapt-if-not blogmore--blog-post-p)]
   ["Links"
    ("l c" "Link to a category" blogmore-link-category :inapt-if-not blogmore--blog-post-p)
    ("l p" "Link to a post" blogmore-link-post :inapt-if-not blogmore--blog-post-p)
    ("l t" "Link to a tag" blogmore-link-tag :inapt-if-not blogmore--blog-post-p)]])
```

With this in place I can simplify my `use-package` quite a bit, just binding
a single key to run `blogmore`.

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
   '(("blog.davep.org" "~/write/davep.github.com/content/posts/")
     ("seen-by.davep.dev" "~/write/seen-by/content/posts/")))
  :bind
  ("<f12> b" . blogmore))
```

Now, when I'm working on a blog post, I can just hit <kbd>F12</kbd>
<kbd>b</kbd> and I get a neat menu:

![BlogMore with all commands available](/attachments/2026/04/04/transient-all.png#centre)

Better still, because of how `transient` works, I can ensure that only
applicable commands are available, while still showing them all. So if I've
not even got a blog selected yet:

![With no commands available](/attachments/2026/04/04/transient-none.png#centre)

Or with a blog selected but not actually working on a post yet:

![With some commands available](/attachments/2026/04/04/transient-some.png#centre)

So far I'm really liking this approach, and I'm tempted to lean into
transient more with some of my packages now. While on the surface it does
seem that it has the downside of the binding choices being dictated by me,
the fact is that the commands are all still there and anyone can use their
own bindings, or I guess override the transient itself and do their own
thing.

[^1]: Yes, it is a bit out of the way on the keyboard, but so is
    <kbd>Esc</kbd>. I find my muscle memory has no problem with it.

[//]: # (2026-04-04-blogmore-el-v2-6.md ends here)
