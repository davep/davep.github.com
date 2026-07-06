---
title: "textual-enhanced v1.6.0"
date: "2026-07-06 10:31:10+0200"
category: Python
tags: [Coding, Python, textual, textual-enhanced]
---

I've just made a small update to
[`textual-enhanced`](https://textual-enhanced.davep.dev/), my core library
used for most of my [Textual](/tag/textual/)-based applications. In v1.6.0
I've extended the "constructor" for
[`ModalInput`](https://textual-enhanced.davep.dev/library-contents/dialogs/#textual_enhanced.dialogs.ModalInput)
to allow passing in optional values for `password`, `suggester`, `title` and
`sub_title`.

Most of the time I just want to quickly call on `ModalInput` to get input
from the user. If I need anything more fancy, I roll my own dialog. But in
some work I'm doing on [Rogallo](/tag/rogallo/), it would be helpful for me
to at least set the `suggester`. So, without adding *every* optional
parameter for the Textual `Input` widget, I've extended what can be passed
in to what I think will be a useful subset for my applications.

[//]: # (2026-07-06-textual-enhanced-v1-6-0.md ends here)
