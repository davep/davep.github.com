---
layout: post
title: macOS desktop widget switching
category: Tech
tags: macOS, fish, shell, streaming
date: 2024-04-17 09:26:00 +0000
---

When [desktop widgets](https://support.apple.com/en-gb/108996) first turned
up in macOS I was pretty quick to embrace them. On my personal Mac Mini I
use a pair of screens, the right one mostly given over to Emacs, and there
was generally room to space there. These days that screen generally looks
something like this:

![The usual layout of my right screen](/attachments/2024/04/17/right-screen.png#centre)

Recently I've got into [streaming while I do some
coding](https://www.youtube.com/@davep-codes/streams) and it's the
right-hand screen that I work on and capture using OBS. When I was setting
this up I realised that the widgets being there could be a problem; not
because they could distract or anything, more that they could, at times,
contain sensitive information (there's my reminder list and my calendar
there after all).

What I needed was a quick method of hiding all the widgets, and showing them
again later, without it being a lot of faff.

With a little bit of digging around on the net I finally came up with a pair
of `fish` abbreviations that do just the job!

```
abbr -g widoff "defaults write com.apple.WindowManager StandardHideWidgets -int 1"
abbr -g widon "defaults write com.apple.WindowManager StandardHideWidgets -int 0"
```

Now, when I'm going to stream, part of my "getting stuff ready to go live"
checklist is to run `widoff` in the terminal; once I'm finished I can then
just run `widon` again to have them come back.

Fast, clean, handy.

I've also got a pair for when I'm using [Stage
Manager](https://support.apple.com/en-gb/guide/mac-help/mchl534ba392/mac):

```
abbr -g smwidoff "defaults write com.apple.WindowManager StageManagerHideWidgets -int 1"
abbr -g smwidon "defaults write com.apple.WindowManager StageManagerHideWidgets -int 0"
```

Although, really, I can't remember the last time I used Stage Manager. I
dabbled with it for a wee while, found it vaguely handy in a couple of
situations, but it doesn't seem to have stuck as part of my workflow or work
environment.

[//]: # (2024-04-17-macos-desktop-widget-switching.md ends here)
