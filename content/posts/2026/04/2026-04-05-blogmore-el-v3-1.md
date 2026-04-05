---
title: blogmore.el v3.1
date: 2026-04-05 20:04:44+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, blogmore.el, coding, EIEIO
---

When [I first started writing
`blogmore.el`](/2026/03/19/some-blogmore-elisp.html) it was just going to be
a handful of commands that let me spin up a new blog post, and insert the
odd link here and there when needed. Initially it only handled a single
blog, and everything it did was based around how I lay my personal blog out,
and was also very much geared to how I'd made
[BlogMore](https://blogmore.davep.dev/) work.

But then I wanted to use it to edit both my personal blog *and* my
[photoblog](https://seen-by.davep.dev/). So then I had to add support for
configuring different ways of laying out posts for different blogs, etc.

Still, it was mostly written as a personal tool that worked for my stuff. I
*tried* to make it so that it was easy enough to configure (and let's be
fair: it's for Emacs and written in [Emacs Lisp](/tag/emacs-lisp/), it's
kind of hard to not be very configurable if you're happy to get your hands
dirty with some coding), but there were still some parts of it that weren't
as easy to change as I'd have liked.

Also, when I'd originally added the multi-blog configuration, I'd chosen a
format for the list of blogs that was an assoc-list of pure lists wrapped by
a `cl-defstruct` to make for easier access. It worked well but was very
positional in its nature.

So when [the request came
in](https://mastodon.me.uk/@andyc/116348654225582976) to be able to have
better control over the name of the file when starting a new post, which
meant I was going to need to rearrange the structure again, it was time to
try and do something about it.

Which is how I'm now on v3.1 (yes, there was a
[v3.0](https://github.com/davep/blogmore.el/releases/tag/v3.0) but I quickly
found something in that that needed fixing[^1]). It's a major version bump
because I've totally changed how the `blogmore-blogs` variable holds the
data.

From now on I'm using
[EIEIO](https://www.gnu.org/software/emacs/manual/html_node/eieio/) to
create a class that holds all of the data for a given blog. This, I believe,
makes the code easier to read and should also make it more resilient to the
addition of any new properties. Also thanks to [how such classes can work
with the customize
system](https://www.gnu.org/software/emacs/manual/html_node/eieio/Customizing.html)
the `customize` experience remains pretty much the same too.

Personally I don't use the `customize` UI, instead I declare everything
via `use-package`. As of the time of writing my declaration for `blogmore`
looks like this:

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
   (list
    (blogmore-blog
     :title "blog.davep.org"
     :posts-directory "~/write/davep.github.com/content/posts/"
     :post-subdirectory-function (lambda () (format-time-string "%Y/%m/")))
    (blogmore-blog
     :title "seen-by.davep.dev"
     :posts-directory "~/write/seen-by/content/posts/")))
  :bind
  ("<f12> b" . blogmore))
```

There's a bunch of other changes and tweaks under the hood in this release
too. All of these should come together to make `blogmore.el` a little more
configurable than it was before. I think, to get the best out of it, anyone
wanting to configure it "just so" for their purposes will still have to do a
little bit of work, which makes me want to spend some time soon writing some
proper documentation, complete with examples of how you might achieve
different things.

One big change I've made under the hood is to the code that is used when you
insert a link to a post (`blogmore-link-post`). When this runs it lets me
pick a file in your filesystem that is a post from my currently-active blog.
Once it has the filename it needs to turn it into a root-relative link. So
this:

```
~/write/davep.github.com/content/posts/2026/04/01/2026-04-01-foo.md
```

needs to become:

```
/2026/04/01/foo.html
```

Until now I just did some regexp faffing that took the `2026-04-01-` at the
start of the filename and swapped each `-` for `/`. Nice and easy. Simple
enough to code up and get things working a few weeks back. Not at all
flexible.

So as a proof-of-concept of how sophisticated someone could get with
configuring this I've changed `blogmore-default-post-maker-function` from
this:

```elisp
(defcustom blogmore-default-post-maker-function
  (lambda (file)
    (replace-regexp-in-string
     (rx bos (group (+ digit)) "-" (group (+ digit)) "-" (group (+ digit)) "-")
     "\\1/\\2/\\3/"
     (file-name-base (file-name-sans-extension file))))
  "Default function to generate a link for a blog post from its filename."
  :type 'function
  :group 'blogmore)
```

and turned it into this:

```elisp
(defcustom blogmore-default-post-maker-function
  (lambda (file)
    (format
     "%s/%s"
     (format-time-string
      "%Y/%m/%d"
      (with-temp-buffer
        (insert-file-contents-literally file)
        (parse-iso8601-time-string
         (blogmore--clean-time-string (blogmore--get-frontmatter-property "date")))))
     (replace-regexp-in-string
      (rx bol (= 4 digit) "-" (= 2 digit) "-" (= 2 digit) "-")
      ""
      (file-name-base file))))
  "Default function to generate a link for a blog post from its filename."
  :type 'function
  :group 'blogmore)
```

So whereas before I was simply messing with the file's name, now I'm loading
the `date` frontmatter from the chosen file and using *that* to create the
date portion of the path in the URL that I use on my blog. The benefit here
is that someone might want to keep the date portion of the path in the URL,
but never want it as part of the Markdown source file's name, and so this
change means they can call the file anything they want; it doesn't look at
that but instead uses the actual date from the post's frontmatter.

I think this nicely demonstrates that, especially thanks to how powerful
Emacs and Emacs Lisp are, it's fairly easy to make `blogmore.el` work just
the way you want. I *think* I've provided almost all the hooks necessary to
configure it all sorts of ways, but if you do happen to use it and run into
something I might have missed, [let me
know](https://github.com/davep/blogmore.el/issues).

[^1]: I have at least two slightly different `date` formats going on in my
    Markdown and Emacs' `parse-iso8601-time-string` is kind of picky. So I
    [added a function to try and clean that
    up](https://github.com/davep/blogmore.el/pull/57/changes).

[//]: # (2026-04-05-blogmore-el-v3-1.md ends here)
