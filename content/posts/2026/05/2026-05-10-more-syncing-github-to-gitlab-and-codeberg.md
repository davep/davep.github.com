---
title: More syncing GitHub to GitLab and Codeberg
date: 2026-05-10 08:58:21+0100
category: Coding
tags: Codeberg, Coding, FOSS, GitHub, GitLab, backups, git
---

Following on from [my first post about
this](/2026/05/08/syncing-github-to-gitlab-and-codeberg.html), I've tweaked
[the script I'm using to backup a repo to GitLab and
Codeberg](https://github.com/davep/setup-forge-sync):

```sh
#!/bin/sh

# Check if the current directory is a Git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Error: This directory is not a Git repository."
    exit 1
fi

REPO_NAME="$1"

# If no repository name was provided, try to get it from the origin remote
if [ -z "$REPO_NAME" ]; then
    ORIGIN_URL=$(git remote get-url origin 2>/dev/null)
    if [ -n "$ORIGIN_URL" ]; then
        REPO_NAME=$(basename -s .git "$ORIGIN_URL")
    else
        echo "Error: No repository name provided and no 'origin' remote found."
        echo "Usage: $0 <repo-name>"
        exit 1
    fi
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

# Also backup all tags.
git config --add remote.backups.push 'refs/tags/*:refs/tags/*'

echo "----------------------------------------------------"
echo "Backups configured:"
git remote -v
echo "----------------------------------------------------"
echo "To perform the initial sync, run: git push backups"

### setup-forge-sync ends here
```

The changes from last time include:

- The repo name now defaults to whatever is used for GitHub, so I don't have
  to copy/paste it or type it out.
- It now backs up all the tags too.

I've been running with this for a couple of days now and it's proving really
useful. Well, when [Codeberg](/tag/codeberg/) is available to push anything
to...

[//]: # (2026-05-10-more-syncing-github-to-gitlab-and-codeberg.md ends here)
