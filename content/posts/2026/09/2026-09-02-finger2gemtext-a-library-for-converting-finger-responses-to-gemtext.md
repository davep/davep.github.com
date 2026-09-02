---
title: "finger2gemtext - A library for converting finger responses to Gemtext"
date: "2026-09-02 19:21:50+0100"
category: Python
tags: [Coding, "Gemini Protocol", PyPI, Python, finger, gemtext, finger2gemtext, smolweb]
---

I've just released the first version of another library in the collection of
libraries that support the development of
[Rogallo](https://rogallo.davep.dev/): specifically, another one that helps
convert text in other formats into [Gemtext](/tag/gemtext/) so Rogallo's
display can be a little richer. In effect, this is a sibling to
[`md2gemtext`](https://md2gemtext.davep.dev/) and
[`html2gemtext`](https://html2gemtext.davep.dev/).

This time it's a library to convert [finger](/tag/finger/) responses into
Gemtext, where it makes sense. For the most part, finger responses are
free-form plain text, but there are times when there's information in the
response that would be of most use if you could interact with it. For
example, if you get a user list from `plan.cat`[^1], that's a lot of data
that could be turned into `finger://` URIs that can be subsequently
followed.

With this in mind, [`finger2gemtext`](https://finger2gemtext.davep.dev/) can
take a body of text, look at it to see if it might be possible to convert it
to useful Gemtext, and will convert it if that's the case. Given that
there's no standard to be had here, and given that any given response could
be of any form the author desires, I'm making the conversion pretty
conservative.

What I have done, though, is make it so that the conversion process can be
extended. The [`finger_to_gemtext`
function](https://finger2gemtext.davep.dev/finger2gemtext/#finger2gemtext.finger_to_gemtext)
can be given a collection of additional filtering classes; if the built-in
classes can't find anything to convert, the additional classes get a go.
There is [a base class to inherit
from](https://finger2gemtext.davep.dev/finger2gemtext/#finger2gemtext.FingerFilter).

I've not fully planned it out yet, but the vague idea I have here is that
Rogallo could, at some point, have *"finger plugins"* which will handle
various special cases and site-specific formats.

For now, though, this gives me the basics that let me turn this:

![A plain finger response](/attachments/2026/09/02/plain-finger.webp#centre)

into something where I can follow `finger://` links without the need to
copy/paste/edit:

![A richer finger response](/attachments/2026/09/02/rich-finger.webp#centre)

Now I need to find a few more online finger resources that respond with
things worth making linkable...

[^1]: `finger @plan.cat`

[//]: # (2026-09-02-finger2gemtext-a-library-for-converting-finger-responses-to-gemtext.md ends here)
