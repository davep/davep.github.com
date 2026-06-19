---
title: "Gemini client rendering"
date: "2026-06-19 20:06:45+0100"
category: Coding
tags: [Coding, "Gemini Protocol", Python, smolweb, textual]
cover: "/attachments/2026/06/19/gemini-client-cover.webp"
---

Yesterday [I got the basic framework of my Gemini client up and
going](/2026/06/18/gemini-client-basic-framework.html), and this evening
I've been working on getting rendering of the gemtext in place. It's not the
most tricky format to handle, so the parser and Textual widget to display
the result have come together pretty quickly.

![Browsing with the client](/attachments/2026/06/19/gemini-client.gif#centre)

With this in place I've got the core of a working client now. Next up is
going to be adding history with forward and backward navigation, then after
that things like bookmarks and so on.

[//]: # (2026-06-19-gemini-client-rendering.md ends here)
