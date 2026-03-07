---
layout: post
title: Helping myself change the default git branch
category: Coding
tags: git
date: 2020-07-09 20:17:00+0100
---

This is something I've being meaning to do for a couple or so years now, and
unsurprisingly it's bubbled up again recently: the business of swapping the
name of the `master` branch in `git` out for something better.

Because it's one of those jobs that's simultaneously simple and also
laborious, I kept putting it off. Changing up the local configuration so
that `main` (or whatever name you prefer) is used "out of the box" [is
simple enough](https://leigh.net.au/writing/git-init-main/); the laborious
part is updating all of the repositories that live in the "forge of choice".
In my case, [over on GitHub](https://github.com/davep), I have [getting on
for 200 repositories](https://github.com/davep?tab=repositories) -- 142 of
which are public (as of the time of writing). At work we use
[GitLab](https://gitlab.com/) as our internal forge and I've got a
non-trivial number of repositories on there too.

The obvious first step to tackling this is to knock up a little tool to help
find the repos that still need swapping. That was [simple
enough](https://github.com/davep/git-archaic):

```bash
#!/bin/bash

# Quick and dirty tool to find repositories that still make use of a
# "master" branch. Helps with tracking down the ones that need
# updating/improving.

for repo in $(find . -name .git)
do
    (
        cd "$(dirname $repo)"

        if git branch | grep master > /dev/null 2>&1
        then
            echo "$(dirname $repo)"
        fi
    )
done

### git-archaic ends here
```

It's not meant to be clever, just something I can run when I'm in a "default
branch swapping" mood so find a repository or two to tackle. The idea being
that it uses `find` to pull out any instance of `.git` in or below the
current directory, changes to it (inside a sub-process to ensure the `PWD`
gets put back after the `cd` that happens, before the next iteration of the
loop), gets a list of the branches and, if `master` is one of them, prints
the directory name.

Using this, I can now slowly work through my more active repositories and
make the swap -- the idea being that if I currently have them cloned down to
my machine, they're obviously some level of "active". At some point I
imagine I could get more clever and use the APIs of the forges to look at
all the repositories I own; that's another job for another day.

This gives me enough to be going on with. :-)

[//]: # (2020-07-09-helping-myself-change-the-default-git-branch.md ends here)
