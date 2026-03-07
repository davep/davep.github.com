---
layout: post
title: textual-countdown
category: Python
tags: PyPi, Python, coding, Textual
date: 2024-01-11 22:52:00 +0100
---

The idea for this one popped into my head while on the bus back from Textual
Towers this evening. So after dinner and some nonsense on TV I had to visit
my desk and do a quick hack.

This is [`textual-countdown`](https://github.com/davep/textual-countdown), a
subtle but I think useful countdown widget for Textual applications.

![Textual Countdown in action](/attachments/2024/01/11/textual-countdown.gif)

The idea is that you compose it somewhere into your screen, and when you
start the countdown the bar highlights and then starts to shrink down to
"nothing" in the middle of its display. When the countdown ends a message is
posted so you can then perform the task that was being waited for in an
event handler.

Not really a novel thing, I've seen this kind of thing before on the web;
I'm sure we all have. I just thought it would be a fun idea for Textual
applications too.

I envisage using this where, perhaps, an application needs to wait for an
API-visiting cooldown period, or perhaps as a subtle countdown for a
question in a quiz; something like that.

Anyway, if this sounds like it's something useful for your Textual
applications, [it's now available from
PyPi](https://pypi.org/project/textual-countdown/) and, of course, the
source is over [on GitHub](https://github.com/davep/textual-countdown).

[//]: # (2024-01-11-textual-countdown.md ends here)
