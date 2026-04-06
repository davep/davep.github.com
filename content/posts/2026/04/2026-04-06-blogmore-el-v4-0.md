---
title: blogmore.el v4.0
date: 2026-04-06 17:04:16+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, blogmore.el, coding
cover: /attachments/2026/04/06/remove-tag.png
---

Despite having bumped it from 2.x to 3.x
[yesterday](/2026/04/05/blogmore-el-v3-1.html), I'm calling
[v4.0](https://github.com/davep/blogmore.el/releases/tag/v4.0) on
[`blogmore.el`](https://github.com/davep/blogmore.el) today. There's a good
reason for this though. While tinkering with some of the configuration
yesterday, and also answering a configuration question last night, I
realised that it made sense to make some of the internals into public
utility functions.

Now, sure, [Emacs Lisp](/tag/emacs-lisp/) doesn't really have *internals* in
the private function sense, but I've always liked the approach that a
`package--` prefix communicates *"internal, might go away"* vs `package-`
which tells me *"this is a stable part of the API of this package"*. With
this in mind I've always tried to write my code using this convention. I did
this with `blogmore.el` too and a *lot* of the code had the `blogmore--`
prefix.

There's plenty of code in there that someone might want to make use of, if
they wanted to add their own commands, or do fun things with the
configuration. So with this in mind I've "promoted" a bunch of code to being
"public" and, in that case, I feel this deserves another major version
bump[^1].

Things that are now part of the "public" interface include:

- `blogmore-clean-time-string`
- `blogmore-get-frontmatter`
- `blogmore-remove-frontmatter`
- `blogmore-set-frontmatter`
- `blogmore-slug`
- `blogmore-toggle-frontmatter`
- `blogmore-with-post`

Each one is documented via its docstring (just a quick
<kbd>Ctrl</kbd>+<kbd>h</kbd> <kbd>f</kbd> `function-name` <kbd>RET</kbd>
away) and hopefully is pretty self-explanatory.

`blogmore-with-post` is especially handy as it provides a quick and easy way
of pulling information from a post file. So something like this:

```elisp
(blogmore-with-post "~/write/davep.github.com/content/posts/2026/04/2026-04-05-blogmore-el-v3-1.md"
  (list
   (blogmore-get-frontmatter "title")
   (blogmore-get-frontmatter "date")))
```

resulting in:

```elisp
("blogmore.el v3.1" "2026-04-05 20:04:44+0100")
```

Meaning that this snippet from [yesterday's
post](/2026/04/05/blogmore-el-v3-1.html):

```elisp
(with-temp-buffer
  (insert-file-contents-literally file)
  (parse-iso8601-time-string
   (blogmore--clean-time-string (blogmore--get-frontmatter-property "date"))))
```

becomes:

```elisp
(blogmore-with-post file
  (parse-iso8601-time-string
   (blogmore-clean-time-string (blogmore-get-frontmatter "date"))))
```

Not massively different, but it reads better and now all the calls are to
the "public API" of the package.

Not all the changes are "promoted internals". I've also added a
`blogmore-remove-tag` command (and also added it to the transient menu).

![Removing a tag](/attachments/2026/04/06/remove-tag.png#centre)

I've also changed the way that `blogmore-add-tag` works so that, now, if
it's called from the transient, it immediately goes back to the tag input
prompt, allowing for another tag to be immediately selected (you can quit
out of this with <kbd>Ctrl</kbd>+<kbd>g</kbd>). Removal of a tag works in a
similar way, making things a lot quicker.

I've also added some extra tests too, which makes it even easier for me to
make future changes with confidence. The more I work with it the more I
appreciate that
[ERT](https://www.gnu.org/software/emacs/manual/html_mono/ert.html) is
available.

[^1]: Ordinarily it shouldn't matter as the public interface isn't changing,
    but some of the "internal" functions had been mentioned as options for
    configuration.

[//]: # (2026-04-06-blogmore-el-v4-0.md ends here)
