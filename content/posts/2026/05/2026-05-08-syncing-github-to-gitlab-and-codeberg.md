---
title: Syncing GitHub to GitLab and Codeberg
date: 2026-05-08 08:25:03+0100
category: Coding
tags: Codeberg, Coding, FOSS, GitHub, GitLab, backups, git
---

I've had a [GitLab account](https://gitlab.com/davep) since December 2017.
This came about [because of the new job I started in January
2018](/2017/12/12/on_to_something_new.html). They used a self-hosted
internal instance of GitLab for all their code, so it made sense I get
familiar with it (it wasn't hard; especially back in 2017 it was near enough
a clone of GitHub in terms of what it did). Since then, though, I've never
really done anything with it. I think I had a repo or two on there for a
short while, but I must have nuked them at some point because the account
has been empty for the longest time.

A [Codeberg](https://codeberg.org/davep) account, on the other hand, [only
got created the other day](/2026/05/06/trying-out-codeberg.html). Having
created this, I got to thinking about how I might use it. In doing so I
thought back to my GitLab account and then also got to thinking about where
all my public code lives, and how "safe" it is.

Now, sure, the whole point of [Git](/tag/git/) is that it's distributed.
Forges are a useful thing to have and work with, but they shouldn't be *the*
place where your code lives. On the other hand, I've had so many machines,
and so many work environments, that it has become the case that [my GitHub
account](https://github.com/davep) has become *the* storage location for my
code and projects.

Mostly this is fine. If GitHub were to disappear tomorrow I imagine we'd all
have bigger things to be worrying about anyway. But the principle stands:
why not distribute the load? Why not distribute the effort when it comes to
sharing code I write?

So yesterday I finally decided on a plan: for the moment at least, I'm going
to keep using GitHub as my "primary" location for working on stuff. It's
where I'll have WiP branches, it's where I'll keep issues, it's where I'll
encourage people to raise requests and stuff, it's where I'll host this
blog. But I'm going to start syncing projects to both GitLab and Codeberg. I
see this as having two benefits: anyone who doesn't want to interact with
GitHub can now easily fork code, and if they wish they can raise issues and
the like too. Meanwhile, in doing this, I'll also have the added benefit of
my code being "backed up" in at least three different locations[^1].

The approach I've settled on, for the moment, is based around [this little
shell script](https://github.com/davep/setup-forge-sync):

```sh
#!/bin/sh

# Check if a repository name was provided
if [ -z "$1" ]; then
    echo "Error: No repository name provided."
    echo "Usage: $0 <repo-name>"
    exit 1
fi

REPO_NAME="$1"

# Check if the current directory is a Git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Error: This directory is not a Git repository."
    exit 1
fi

echo "Configuring multi-forge backup sync for: $REPO_NAME"

# Set up the remote called backups. Anchor it to Codeberg.
git remote remove backups > /dev/null 2>&1
git remote add backups "ssh://git@codeberg.org/davep/${REPO_NAME}.git"

# Set up the push URLs.
git remote set-url --push backups "ssh://git@codeberg.org/davep/${REPO_NAME}.git"
git remote set-url --add --push backups "git@gitlab.com:davep/${REPO_NAME}.git"

# Only ever backup main.
git config remote.backups.push refs/heads/main:refs/heads/main

echo "----------------------------------------------------"
echo "Backups configured:"
git remote -v
echo "----------------------------------------------------"
echo "To perform the initial sync, run: git push backups main"

### setup-forge-sync ends here
```

I'm going to keep all repo names the same[^2]. So when I use this script
it'll set things up so I can `git push backups` and `main` will then get
pushed up to both GitLab and Codeberg. I don't feel the need to be keeping
any WiP branches in sync or kicking about, likewise any `gh-pages` branches.

While I'm sure I could have done something a little more automated, this
feels like a neat and simple approach, and also allows me to curate what
appears in the two other places over time (I suppose, eventually, I'll
mirror everything that isn't a dead experimental repo, but meanwhile I'll
prioritise projects that are either still very useful or which I'm actively
developing and maintaining).

[^1]: Yes, I have other backups too, but they're always
    current-working-machine type backups.
[^2]: Except, perhaps, for any repo whose name starts with `.`; I seem to
    recall that GitLab can't handle that, for some bizarre reason. Perhaps
    that's fixed now?

[//]: # (2026-05-08-syncing-github-to-gitlab-and-codeberg.md ends here)
