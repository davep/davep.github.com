---
title: Stopping an accidental push
date: 2026-05-13 19:04:49+0100
category: Emacs
tags: Emacs, Emacs Lisp, Magit, backups, git
---

After starting to make use of [the GitLab/Codeberg sync
approach](/2026/05/10/more-syncing-github-to-gitlab-and-codeberg.html) for
various repositories, I found that my muscle memory in
[Magit](https://magit.vc/) was getting the better of me and, on occasion,
I'd push a new branch to `backups` when I wanted `origin`. I sensed there
had to be a way round that.

Here's what I settled on:

```elisp
(advice-add
 'magit-list-remotes
 :filter-return (lambda (remotes) (delete "backups" remotes)))
```

Now I never see `backups` in Magit and now I can keep using my muscle memory
(rather than actually reading what is in front of me, it seems).

[//]: # (2026-05-13-stopping-an-accidental-push.md ends here)
