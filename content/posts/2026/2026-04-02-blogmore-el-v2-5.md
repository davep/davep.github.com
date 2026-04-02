---
title: blogmore.el v2.5
date: 2026-04-02 20:53:09+0100
category: Emacs
tags: BlogMore, Emacs, Emacs Lisp, Lisp, blogmore.el, coding, testing
---

Following on from [yesterday's release](/2026/04/01/blogmore-el-v2-4.html),
I've bumped [`blogmore.el`](https://github.com/davep/blogmore.el) to v2.5.
The main change to the package is the thing I mentioned yesterday about the
toggle of the `draft` status. The `draft` toggle yesterday was pretty
simple, with it working like:

- If there is no `draft` frontmatter, `draft: true` is added
- If there is any `draft` frontmatter, it is removed

This meant that if you had `draft: false` set and you went to toggle, it
would be removed, which is the same as setting it to `draft: false`.

Unlikely to generally be an issue, but I also couldn't let that stay like
that. It bothered me.

So now it works as you'd expect:

- If there is no `draft` frontmatter, `draft: true` is added
- If `draft: true` is there, it is removed
- If `draft: false` is there, it is set to `draft: true`

Much better.

Another change is that I fixed a problem with older supported versions of
Emacs. I didn't know this was a problem because I'm running 30.2 everywhere.
Meanwhile, thanks to `package-lint-current-buffer` from
[`package-lint.el`](https://github.com/purcell/package-lint), I have:

```
Package-Requires: ((emacs "29.1"))
```

in the metadata for the package. Turns out though that
[`sort`](https://www.gnu.org/software/emacs/manual/html_node/eintr/Sorting.html)
used to require two parameters (the sequence and the predicate), whereas now
it's fine with just one (it will accept just the sequence and will default
the predicate). So of course `blogmore.el` was working fine for me, but
would have crashed for someone with an earlier Emacs.

As for how I found this out... well I finally, for the first time ever,
dived into using
[ERT](https://www.gnu.org/software/emacs/manual/html_node/ert/index.html) to
write [some
tests](https://github.com/davep/blogmore.el/blob/34ed59bbe11d31b10382c244188bc3afb7c2f8d8/blogmore-tests.el).
While I've used testing frameworks in other languages, I'd never looked at
this with [Emacs Lisp](/tag/emacs-lisp/). It works a treat and is great to
work with; I think I'll be using this a lot more from now on.

Having got tests going I realised I should run them with GitHub actions,
which then meant I managed to discover
[`setup-emacs`](https://github.com/marketplace/actions/set-up-emacs). Having
found this the next logical step was to [set up a matrix test for all the
versions of Emacs I expect `blogmore.el` to work
on](https://github.com/davep/blogmore.el/blob/34ed59bbe11d31b10382c244188bc3afb7c2f8d8/.github/workflows/tests.yml).
This worked fine, except... it didn't. While the tests worked locally, they
were failing for some Emacsen over on GitHub.

And that's how I discovered the issue with `sort` on versions earlier than
the one I'm using locally.

All in all, that was a good little period of hacking. New things discovered,
the package improved, and a wider range of support for different versions of
Emacs.

[//]: # (2026-04-02-blogmore-el-v2-5.md ends here)
