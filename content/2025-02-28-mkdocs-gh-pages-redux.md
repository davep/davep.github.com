---
layout: post
title: MkDocs/mkdocstrings 404 CSS TIL update
category: Coding
tags: documentation, GitHub, mkdocs, mkdocstrings, gh-pages
date: 2025-02-28 22:23:00 +0000
---

Following on from [my post this
morning](/2025/02/28/documenting-fspicker.html), regarding the problem I was
having with `_mkdocstrings.css` being 404 any time I deployed by
documentation, build with `mkdocs`/`mkdocstrings`, to GitHub Pages...

It's come to light that I was doing this on hard mode, pretty much.

While trying to figure out the best way of deploying the docs, I'd stumbled
on `ghp-import` and had been using that. On the other hand, MkDocs has it's
own command for doing the same thing: [`mkdocs
gh-deploy`](https://www.mkdocs.org/user-guide/deploying-your-docs/).

Timothée [pointed out to
me](https://github.com/mkdocstrings/mkdocstrings/discussions/742#discussioncomment-12351028)
that he never runs into this problem, but he used this command. As it turns
out, if you use `mkdocs gh-deploy` it creates the `.nojekyll` file by
default.

And how does it do this? It uses the `ghp-import` code [and uses a switch it
has to achieve exactly
this](https://github.com/mkdocs/mkdocs/blob/4c7404485f988f409ccaf42fefe705222ff5965a/mkdocs/commands/gh_deploy.py#L138).
In fact... the command line version even has a switch for it!

```text
-n, --no-jekyll      Include a .nojekyll file in the branch.
```

This is off by default, when you run the command itself, but I wish I'd
noticed this when I was first experimenting. O_o

Anyway, thanks to Timothée's pointers, I've now managed to [simplify how I
build and publish the docs from
`textual-fspicker`](https://github.com/davep/textual-fspicker/pull/39/files),
and I'll apply this to other projects too.

[//]: # (2025-02-28-mkdocs-gh-pages-redux.md ends here)
