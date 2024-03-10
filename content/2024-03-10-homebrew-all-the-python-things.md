---
layout: post
title: Homebrew all the Python things
category: Coding
tags: Python, terminal, textual, Homebrew, Makefile
date: 2024-03-10 14:12:00 +0000
---

Over the past year and a half I've written a *lot* of Python code, and a lot
of that Python code has been Textual applications; most of those Textual
applications have been very quick demonstration or test applications built
to help support someone asking for help; some of them have been less-trivial
applications written in my own time and for my own use and amusement. Of
them I'd say there are two near-daily-drivers, and a couple that I either
have more plans for, or like to maintain just for the hell of it.

Those latter applications are all ones that [I've deployed to
PyPI](https://pypi.org/user/davepearson/), and because of that are all ones
that I've recommenced be installed using
[`pipx`](https://pipx.pypa.io/stable/). During that time though I've had
half an inclination to make them [installable via
Homebrew](https://brew.sh/). While probably not installable from the core
Homebrew repository[^1], at least installable from a "tap"[^2] that's under
my own GitHub account or something.

To this end I've had [a blog post about packaging Python apps for
Homebrew](https://til.simonwillison.net/homebrew/packaging-python-cli-for-homebrew)
saved in Pinboard for a while now, and every time I look at it I think
*"this is a lot of faff, maybe later"*. Today was that "later".

As it turned out, it was *way* easier than I first realised. The evolution
of today pretty much went like this:

## Deciding to use a single repository as the "tap"

The blog post above seemed to suggest that for every application repository
you want a tap for, you probably want a parallel `homebrew-`-prefixed
repository. This in turn would suggest that every time someone wants to
install one of your tools, they'd need to add a new tap[^3]. As I looked at
it this seemed like way too much faff, so in the end I decided [to create a
single repository that I'd keep all my formula files
in](https://github.com/davep/homebrew-homebrew). The naming of
`homebrew-homebrew` meant that the tap name would simply be
`davep/homebrew`.

Simple and clean, I think: things for homebrew, things that can be installed
via homebrew, that come from davep. To add the tap it's simply:

```sh
$ brew tap davep/homebrew
```

## Ensuring that all my applications and libraries publish source

Although it seems that it might be (possibly, maybe, perhaps, who can tell?)
deprecated, it looked like
[`homebrew-pypi-poet`](https://github.com/tdsmith/homebrew-pypi-poet) was a
tool I'd need to do all the heavy work on making the formula file. A quick
test threw up a problem where it was complaining that my test package (one
of my own applications) didn't have an `sdist`. Sure enough, through nothing
more than never having bothered to make it happen, the source of my
libraries and applications wasn't been uploaded to PyPI when I published.

So I went through some of my repositories and fixed that, making patch
releases as I went.

## Making a `Makefile` to let me be lazy

The next thing to do was to figure out the most lazy way of building the
formula files. From what I could see the main steps to making all of this
work were:

- Make a venv and activate it
- Install `homebrew-pypi-poet`
- Install the package you want to package for Homebrew
- Run `poet` to make the formula

Seemed simple enough. For all sorts of lazy reasons I still tend to use
`pipenv` to get things done quickly, and that seemed to work fine here too.
I'm also a fan of `PIPENV_VENV_IN_PROJECT=true` which makes things clean and
tidy, so I figured a rule in a `Makefile` like this:

```Makefile
clean:
        rm -rf .venv
        rm -f Pipfile Pipfile.lock
        pipenv --python 3.12
        pipenv install --dev homebrew-pypi-poet
```

would be fine to make a clean venv ready to build the formula, and then I'd
have a rule for the package itself that depended on the above, like this:

```Makefile
oshit: clean
        pipenv install oshit
        pipenv run poet -f oshit > Formula/oshit.rb
```

## Fixing the package description

The above was great, and worked really well. But there was one issue that I
could see: the resulting formula file always had this `desc` inside it:

```ruby
desc "Shiny new formula"
```

From what I could see there was no way to tell `poet` what I wanted the
description to be, and neither did I want to have to remember to edit that
line each time I regenerated the formula file. So `sed` to the rescue then I
guess, with this sort of thing:

```sh
sed -i '' 's/Shiny new formula/The actual text I want/' Formula/coolapp.rb
```

## The result

The result of all of this is that I now have [a repository that I or anyone
else can use as a tap](https://github.com/davep/homebrew-homebrew) to be
able to install my stuff using the `brew` command. So now if you want a
little Hacker News reader for the terminal but you don't want to be messing
with installing `pipx` and the like, but you do use `brew` on your machine,
it's just this:

```sh
$ brew tap davep/homebrew
$ brew install oshit
```

Fingers crossed it all "just works" when I next upgrade one of those
packages. I will, of course, have to remember to go into
`davep/homebrew-homebrew` and `make the-app` for the relevant application,
and then commit and push the changes, but that's really not too difficult to
remember and do.

Hopefully it'll then all just work.

[^1]: I do actually [have one package in
    Homebrew](https://formulae.brew.sh/formula/eg), but it wasn't me who put
    it there.
[^2]: I really like Homebrew as a tool for getting stuff installed, by oh my
    gods the naming of things in its ecosystem is terrible and confusing!
[^3]: No, really, I mean it, this naming convention is kinda cringe right?

[//]: # (2024-03-10-homebrew-all-the-python-things.md ends here)
