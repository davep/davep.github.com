---
layout: post
title: Cmd-Tab switcher on all screens
category: TIL
tags: Apple, Mac, macOS, Work
date: 2023-07-14 07:56:00 +0100
---

This week, on Monday gone in fact, [we](https://www.textualize.io/) moved
office. We've now got a bigger space and, as part of that, bigger desks.
Somewhat (but not entirely) coincidentally the work desk will also convert
into a standing desk[^1]. Also also... I inherited a second screen for the
desk too. Ever since the days of CRTs and video cards that supported it,
I've been a fan of having at least a couple of screens in front of me, and
now at my work desk I've got 3 (two external displays and the display of the
MacBook Pro itself).

This caused a slight problem though: horizontally there's quite the spread
of things to look at. This is fine, mostly I'm looking at the screen that's
in front of me; the MacBook is to the left and the "second" screen is to the
right, both with "other" stuff on them. In front of me is Emacs and my
browser, which I flip between lots.

The problem is this: the MacBook needs to go to the left (because of
physical layout), which means that despite me setting the screen in front of
me as the "main" screen, the <kbd>Cmd</kbd>-<kbd>Tab</kbd> display (you know
the thing: when you hit <kbd>Cmd</kbd>-<kbd>Tab</kbd> you see the icons of
all your active applications) appears on the left-most display, which is the
MacBook.

Not great. If I'm looking at the right-most display, and want to switch
using the keyboard, I've got to look over to the left, as a worst case. That
makes for a lot of unnecessary head-swivelling.

One quick Google later and *Today I Learnt* that the following pretty much
solves the problem:

```sh
$ defaults write com.apple.Dock appswitcher-all-displays -bool true
$ killall Dock
```

As the name of the setting would suggest: once done, the switcher appears on
*all* displays.

That's perfect.

[^1]: Although the work one is manual hand-cranked, not electronic
    button-push goodness like [my new one at
    home](2023/07/08/new-desk.html).

[//]: # (2023-07-14-cmd-tab-switcher-on-all-screens.md ends here)
