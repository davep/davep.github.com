---
title: "Port70 - A Gopher protocol library for Python"
date: "2026-07-26 11:32:33+0100"
category: Python
tags: [Coding, PyPI, Python, Rogallo, gopher, smolweb]
---

It was, of course, inevitable that this would happen. After [spinning up
Port79](/2026/07/25/port79-v1-0-0.html) so that I could [add `finger`
support to Rogallo](/2026/07/24/rogallo-v1-1-0.html), it made sense that I
start to think about Gopher support too. So here we go:
[Port70](https://port70.davep.dev/), a similar library for async interaction
with Gopher servers.

This is going to be a bit of an adventure for me. While I'm long familiar
with the existence of Gopher, and I'm fairly certain I used a client once or
twice back in the 90s, I've never really had dealings with the protocol so
know very little about it. Which is a good thing: something new (old?) to
learn.

My plan with this is to add the `GopherURI` class to [the list of URI
types](https://github.com/davep/rogallo/blob/7ea4abaddb542e0cc9baa5ddb88d24836cf2bdec/src/rogallo/types.py#L17-L19)
that [Rogallo understands and
handles](https://github.com/davep/rogallo/blob/7ea4abaddb542e0cc9baa5ddb88d24836cf2bdec/src/rogallo/screens/main.py#L711-L723)
and then provide a method of displaying and navigating the result. I *think*
the cleanest and easiest way of doing this will be to add some code that
transforms a [menu
response](https://en.wikipedia.org/wiki/Gopher_(protocol)#Source_code_of_a_menu)
into [gemtext](https://gemtext.davep.dev/) and then just let the [viewer
widget](https://github.com/davep/rogallo/tree/main/src/rogallo/widgets/viewer)
display it as normal; each of the links in the menu being turned into
`gopher://` URIs.

This should be fun to play with. I'm looking forward to pulling it all
together.

[//]: # (2026-07-26-port70-a-gopher-protocol-library-for-python.md ends here)
