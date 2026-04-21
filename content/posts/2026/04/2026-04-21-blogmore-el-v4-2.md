---
title: blogmore.el v4.2
date: 2026-04-21 19:27:26+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, blogmore.el, coding
---

Another wee update to [`blogmore.el`](https://github.com/davep/blogmore.el),
with a bump to v4.2.

After [adding the webp helper command](/2026/04/17/blogmore-el-v4-1.html)
the other day, something about it has been bothering me. While the command
is there as a simple helper if I want to [change an individual image to
webp](/2026/04/16/i-should-use-webp.html) -- so it's not intended to be a
general-purpose tool -- it felt "wrong" that it did this one specific thing.

So I've changed it up and now, rather than being a command that changes an
image's filename so that it has a `webp` extension, it now cycles through a
small range of different image formats. Specifically it goes `jpeg` to `png`
to `gif` to `webp`.

With this change in place I can position `point` on an image in the Markdown
of a post and keep running the command to cycle the extension through the
different options. I suppose at some point it might make sense to turn this
into something that *actually* converts the image itself, but this is about
going back and editing key posts when I change their image formats.

Another change is to the code that slugs the title of a post to make the
Markdown file name. I ran into the motivating issue yesterday when posting
some images on [my photoblog](https://seen-by.davep.dev/). I had a title
with an apostrophe in it, which meant that it went from something like
`Dave's Test` (as the title) to `dave-s-test` (as the slug). While the slug
doesn't really matter, this felt sort of messy; I would prefer that it came
out as `daves-test`.

Given that wish, I modified `blogmore-slug` so that it strips `'` and `"`
before doing the conversion of non-alphanumeric characters to `-`. While
doing this, for the sake of completeness, I did a simple attempt at removing
accents from some characters too. So now the slugs come out a little tidier
still.

```elisp
(blogmore-slug "That's Café Ëmacs")
"thats-cafe-emacs"
```

The slug function has been the perfect use for an [Emacs
Lisp](/tag/emacs-lisp/) function I've never used before: `thread-last`. It's
not like I've been avoiding it, it's just more a case of I've never quite
felt it was worthwhile using until now. Thanks to it the body of
`blogmore-slug` looks like this:

```elisp
(thread-last
  title
  downcase
  ucs-normalize-NFKD-string
  (seq-filter (lambda (char) (or (< char #x300) (> char #x36F))))
  concat
  (replace-regexp-in-string (rx (+ (any "'\""))) "")
  (replace-regexp-in-string (rx (+ (not (any "0-9a-z")))) "-")
  (replace-regexp-in-string (rx (or (seq bol "-") (seq "-" eol))) ""))
```

rather than something like this:

```elisp
(replace-regexp-in-string
 (rx (or (seq bol "-") (seq "-" eol))) ""
 (replace-regexp-in-string
  (rx (+ (not (any "0-9a-z")))) "-"
  (replace-regexp-in-string
   (rx (+ (any "'\""))) ""
   (concat
    (seq-filter
     (lambda (char)
       (or (< char #x300) (> char #x36F)))
     (ucs-normalize-NFKD-string
      (downcase title)))))))
```

Given that making the slug is very much a "pipeline" of functions, the
former looks far more readable and feels more maintainable than the latter.

[//]: # (2026-04-21-blogmore-el-v4-2.md ends here)
