---
title: "GopherMap - A simple library for parsing Gopher responses"
date: "2026-07-27 19:20:30+0100"
category: Python
tags: [Coding, PyPI, Python, gopher, smolweb]
---

Having [spun up
Port70](/2026/07/26/port70-a-gopher-protocol-library-for-python.html) as a
support library for my effort to add [gopher](/tag/gopher/) support to
[Rogallo](/tag/rogallo/), the next thing I needed was some code to parse the
"gopher map" responses that you get back from Gopher servers. While this
could have been some code in Rogallo itself, much like with
[Gemtext](https://gemtext.davep.dev/), it seemed sensible to put it in its
own library so it could be useful elsewhere.

So... [GopherMap](https://gophermap.davep.dev/)
[v0.1.0](https://gophermap.davep.dev/changelog/#v010) is a thing. Its main
provision is a [class called
`GopherMap`](https://gophermap.davep.dev/gophermap/#gophermap.GopherMap),
which is used to parse some text you give it. Its [`items`
property](https://gophermap.davep.dev/gophermap/#gophermap.GopherMap.items)
is then a tuple of
[`GopherItem`](https://gophermap.davep.dev/gophermap/#gophermap.GopherItem)
objects. Each one of those objects has [a `type`
property](https://gophermap.davep.dev/gophermap/#gophermap.GopherItem.type)
which can be used to [check the type of the
resource](https://gophermap.davep.dev/gophermap/#gophermap.ItemType).

Because Rogallo heavily relies on MIME types to make decisions about what to
do with content, each `ItemType` has a best-efforts-guess
[`mime_type`](https://gophermap.davep.dev/gophermap/#gophermap.ItemType.mime_type)
associated with it. This will make it pretty straightforward for me to
decide if a resource from a Gopher server is something Rogallo can display.

All of this has prompted me to [have a go at creating my own little Gopher
site](gopher://tilde.team/1/~davep/) to help with testing. As with my [wee
Gemini capsule](gemini://tilde.team/~davep/), this is all thanks to
[tilde.team](https://tilde.team/).

[//]: # (2026-07-27-gophermap-a-simple-library-for-parsing-gopher-responses.md ends here)
