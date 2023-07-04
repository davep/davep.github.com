---
layout: post
title: "When the man page fibs"
categories: []
tags: [ "homebrew", "macos", "unix", "python" ]
date: 2020-07-10 20:58:00+0100
---

Earlier this week something in my development environment, relating to
[Homebrew](https://brew.sh/), Python,
[pyenv](https://github.com/pyenv/pyenv) and
[pipenv](https://pipenv.pypa.io/en/latest/), got updated and broke a handful
of repositories. Not in a way that I couldn't recover from, just in a way
that was annoying, got in the way of my workflow, and needed attention.
*(note to self: how I set up for Python/Django development on a machine
might be a good post in the future)*

Once I was sure what the fix was (pretty much: nuke the virtual environment
and recreate it with `pipenv`, being very explicit about the version of
Python to use) the next step was to figure out how many repositories were
affected; not all were and there wasn't an obvious pattern to it. What was
obvious was that the problem came down to `python` in the `.venv` directory
pointing to a binary that didn't exist any more.

![Screenshot 2020-07-10 at 20.21.15.png](/attachments/2020/07/10/Screenshot 2020-07-10 at 20.21.15.png)

So... tracking down problematic repositories would be simple enough, just
look for every instance of `.venv/bin/python` and be sure it points to
something rather than nothing; if it points to nothing I need to remake the
virtual environment.

I quickly knocked up a script that was based around looking over the results
of a `find`, and initially decided to use `file` to perform the test on
`python`. It seemed to make sense, as I wrote the script I checked the `man`
page for `file(1)` on macOS and sure enough, this exists:

> -E On filesystem errors (file not found etc), instead of handling the error as regular output as POSIX mandates and keep going, issue an error message and exit.

Given that `file` dereferences links by default, that should get me an error
for a broken link, right? Bit hacky I guess, but it was the first thing that
came to mind for a quick bit of scripting and would do the trick. Only...

```sh
$ file -E does-not-exist
file: invalid option -- E
Usage: file [bcCdEhikLlNnprsvzZ0] [-e test] [-f namefile] [-F separator] [-m magicfiles] [-M magicfiles] file...
       file -C -m magicfiles
Try `file --help' for more information.
```

[Wat](https://www.destroyallsoftware.com/talks/wat)?!? But it's right there! It says so in the manual! `-E` is documented right in the manual page! And yet it's not in the valid switch list as put out by the command, *and* it's an `invalid option`. The hell?

So I go back and look at the `man` page again and then I notice it isn't in
the list of switches in the synopsis.

> SYNOPSIS  
>     file [-bcdDhiIkLnNprsvz] [--extension] [--mime-encoding] [--mime-type] [-f namefile] [-m magicfiles] [-P name=value] [-M magicfiles] file  
>     file -C [-m magicfiles]  
>     file [--help]  

I then did the obvious tests. Did I have `file` aliased in some way? No. Was
some other thing that works and acts like `file` in my path? No. Was I
absolutely 100% using `/usr/bin/file`? Yes.

Long story short: it seems the `man` page for `file`, on macOS, fibs about
what switches it supports; it says that `-E` is a valid option, but it's not
there.

What's even odder is the man page says it documents v5.04 of the command,
but `--version` reports v5.37. Meanwhile, if I check on a GNU/Linux box I
have access to, it does support `-E`, reports it in the switches, documents
it in the `man` page (in both the synopsis and in the main body of the page)
and it is v5.25 (and so is its man page).

So that was something like 20 minutes lost to a very small problem, for
which there was no real solution, but was time that had to be spent to get
to the bottom of it.

In the end I went with what I probably should have gone with in the first
place: `stat -L`.

```bash
for venv in $(find . -name .venv)
do
    if ! stat -L "$venv/bin/python" > /dev/null 2>&1
    then
        echo "$(dirname $venv)"
    fi
done
```

And now I have that script in my `~/bin` directory, ready for the next time
Homebrew and friends conspire to throw my day off for a while.

[//]: # (2020-07-10-when-the-man-page-fibs.md ends here)
