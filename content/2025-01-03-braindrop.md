---
layout: post
title: Braindrop
category: Coding
tags: Python, terminal, textual
date: 2025-01-03 16:24:00 +0000
cover: attachments/2025/01/03/braindrop-social-banner.png
---

![Braindrop](/attachments/2025/01/03/braindrop-social-banner.png)

A touch over a year ago I did the initial work on an application called
[Tinboard](https://github.com/davep/tinboard), a terminal-based client for
the Pinboard bookmarking service. I had a lot of fun building it and it was
an application that I used on a near-daily basis. However, around August
last year [I realised it was time for me to move on from Pinboard and try
something new](/2024/08/18/paindrop.html); based on various recommendations
I settled on [Raindrop](https://raindrop.io/).

As mentioned [in the other blog post](/2024/08/18/paindrop.html), Raindrop
offered more or less everything I had with Pinboard and so the move was
fairly straightforward. The one thing that was missing though was an
application similar to Tinboard.

So, late on last year, with my winter break approaching, I decided to start
from scratch and build a *"Tinboard for Raindrop"*, which I'm calling
[Braindrop](https://github.com/davep/braindrop).

This was going to be a bit of an adventure too. Since [being laid off from
Textualize earlier in 2024](/2024/03/28/goodbye-textualize.html) I'd not
been following its development quite as closely as I used to, and had also
run into some issues and bugs with it since that time; moreover, as well as
various bugs appearing, some breaking changes had also been made. As such
this was going to be a process where I'd wrap my head around what's happened
with the framework over the prior six months or so.

Given all this, over the past couple of weeks I've been spending a few hours
a day doing some for-pleasure coding and v0.1.0 of Braindrop is the result.

![Main display](/attachments/2025/01/03/braindrop-main.png)

As much as possible I've tried to keep the look and feel similar to that of
Tinboard, while also doing my best to avoid some of the *"ah, I wish I
hadn't done it this way"* design decisions I'd made. As of the time of
writing I'm very pleased with the result.

![The edit dialog](/attachments/2025/01/03/braindrop-edit.png)

One thing I did want to do is ensure that the application was as
keyboard-friendly as possible, while also still allowing use of the mouse.
Textual can sometimes get that wrong and I ran into an example of this while
trying to ensure that there's good in-application help. Somewhat recently
Textual added a built-in help system which, sadly, can't easily be used by
and navigated by someone using the keyboard. So instead I've recreated the
help system I built into Tinboard, while adopting the documentation standard
that Textual had settled on (which, coincidentally, was kind of similar to
what I did in Tinboard to start with).

![The help dialog](/attachments/2025/01/03/braindrop-help.png)

As with Tinboard, I've also made sure to make full use of the command
palette, with every action that makes sense having a keyboard hotkey as well
as a command in the palette. I also took things a little further and made
sure that the hotkeys are shown in the command palette for easier discovery.

![The command palette](/attachments/2025/01/03/braindrop-command-palette.png)

I've also made sure that Textual's new theme system is available for easy
use; so out goes dark/light mode toggling and in comes a collection of
different themes. Here's a wee selection as an example:

![Example theme 1](/attachments/2025/01/03/braindrop-theme-1.png)
![Example theme 2](/attachments/2025/01/03/braindrop-theme-2.png)
![Example theme 3](/attachments/2025/01/03/braindrop-theme-3.png)
![Example theme 4](/attachments/2025/01/03/braindrop-theme-4.png)

That's a small selection of the themes, with more to explore.

There's a few more things I want to do before I consider the application
v1.0-ready, but it's already in use by me and working well. As I decide what
else I want to add to it [I'm building up a list of TODO
items](https://github.com/davep/braindrop/issues?q=is%3Aissue+is%3Aopen+label%3ATODO).

Given that my day job these days is quite varied, isn't quite so
coding-intensive, and isn't always related to all things Python, it's
actually been fun to sit down and hack up a pure Python application from
scratch again. It's also helped me discover a couple or so fresh bugs in
Textual (which [I've
reported](https://github.com/Textualize/textual/issues/created_by/davep), of
course) and given me the opportunity to [PR some trivial fixes as I've
noticed typos and stuff as I
go](https://github.com/Textualize/textual/pulls/davep).

Anyway; that's v0.1.0 out in the wild. I'm pleased with how it's turned out
and there's more to come. It's licensed GPL-3.0 and available [via
GitHub](https://github.com/davep/braindrop) and also [via
PyPi](https://pypi.org/project/braindrop/). If you have an environment that
has `pipx` installed you should be able to get up and going with:

```sh
$ pipx install braindrop
```
It can also be installed with
`Homebrew` by tapping `davep/homebrew` and then installing `braindrop`:

```sh
$ brew tap davep/homebrew
$ brew install braindrop
```

I hope this is useful to someone else. :-)

[//]: # (2025-01-03-braindrop.md ends here)
