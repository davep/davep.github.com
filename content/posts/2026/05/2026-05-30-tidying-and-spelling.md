---
title: Tidying and spelling
date: 2026-05-30 11:29:42+0100
category: Meta
tags: Blogging, aspell, awk, writing
---

Since kicking off the work on [BlogMore](https://blogmore.davep.dev/) and
[`blogmore.el`](https://github.com/davep/blogmore.el), I've absolutely found
that I've reduced the friction involved when it comes to writing a quick (or
not so quick) blog post. I've also found that I want to go back and tidy up
lots of my old posts. Over the past few weeks I've gone and cleaned up the
size and positioning of images; [converted most images to WebP
format](/2026/05/15/converted-to-webp.html); cleaned and consolidated the
tags used; hunted down and fixed broken internal links; and a few other
things besides.

Another thing I want to do is go back and hunt down, and clean up, typos and
spelling mistakes, and the like. While I'm careful to try and not make any
errors when typing out a post, and while I've always made a point of reading
my posts back to try and catch problems, I've not always been successful.
Sometimes I'm just blind to the errors, sometimes I'm just rushing. There's
over a decade of mistakes on this blog.

So, with this in mind, I've added a [couple of little
tools](https://github.com/davep/davep.github.com/tree/main/bin) to the
[build environment for this blog](https://github.com/davep/davep.github.com)
to help me go back and catch problems that might need addressing.

The main tool is [a script for running `aspell` over all the Markdown and
building a list of
errors](https://github.com/davep/davep.github.com/blob/main/bin/spellcheck).
This shows the names of the Markdown files that have errors, and lists the
unknown words for them. For example:

```
=== content/posts/2019/2019-11-04-my-pylint-shame.md ===
flycheck
prepending
whitespace

=== content/posts/2020/2020-08-23-the-pep-8-hill-i-will-die-on.md ===
parens
whitespace

=== content/posts/2020/2020-06-22-swift-til-1.md ===
backticks

=== content/posts/2020/2020-06-14-my-journey-to-the-dark-side-is-complete.md ===
Macbook
Macbooks
scrollbars

=== content/posts/2020/2020-01-19-dnote-el.md ===
dnote
Dnote

=== content/posts/2020/2020-01-11-where-i-live-and-work.md ===
adwaita
eshell
powerline
```

This alone makes it nice and easy to go back and clean up some obvious
issues. A problem I ran into though was that I was getting a lot of false
reports for things in the front matter of the files (especially parts of the
`cover:` file name) and also in the end-of-file comments I like to use. So,
with a little help from Gemini (because it's a moment since I last wrote any
`awk` in anger), I wrote [a filter to "clean" the Markdown
content](https://github.com/davep/davep.github.com/blob/main/bin/clean_markdown)
before running it through `aspell`.

Already, using this setup, I've caught a few things that deserved cleaning
up, and because there will be a lot of words that are correct but particular
to this blog and what I write about, [I'm also building up a local ignore
list](https://github.com/davep/davep.github.com/blob/main/.ignore_spelling).

While this setup isn't going to make the content of this blog error-free, it
should give me everything I need to go back and slowly improve some of the
older text, and to harmonise some of the spellings of some technical terms.

[//]: # (2026-05-30-tidying-and-spelling.md ends here)
