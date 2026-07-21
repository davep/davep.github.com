---
title: "Port79 - A finger protocol library for Python"
date: "2026-07-21 16:19:20+0100"
category: Python
tags: [Coding, PyPI, Python, finger, smolweb]
---

Now that [Rogallo](https://rogallo.davep.dev/) is starting to settle down
somewhat, with all the main [Gemini Protocol](/tag/gemini-protocol/) work
falling into place, I've been thinking about adding one or two adjacent
protocols. The two most common and obvious ones are
[Finger](https://en.wikipedia.org/wiki/Finger_(protocol)) and
[Gopher](https://en.wikipedia.org/wiki/Gopher_(protocol)). While I'm still
undecided about adding the latter, the former seems like a fun one to
include (if only because [I've had an account](finger://plan.cat/davep) on
[plan.cat](https://plan.cat/) for around four years now).

With that in mind, much like [I did with
Wasat](/2026/06/17/wasat-a-gemini-protocol-library-for-python.html), I wrote
a spec for what I wanted and pointed [Antigravity](/tag/antigravity/) at it.
The result is [Port79](https://port79.davep.dev/). As well as providing a
library, there's also a small `finger` clone CLI, which can be run with
`python -m port79` (if it's installed as a library) or with `port79` (if
installed along with any command scripts).

```sh
$ port79 davep@tilde.team

hello [removed],

Project:
  Rogallo: https://rogallo.davep.dev/

Plan:
  Currently building gemini://tilde.team/~davep/

Pronouns: he/him

$ port79 davep@plan.cat
Login: davep                            Name: Dave Pearson
Directory: /home/davep                 Shell: /bin/plan.cat
Last login Mon Jul 20 19:06:33 2026 UTC
No Mail.
Plan:
Rogallo v0.12.0, with some more QoL changes:
https://blog.davep.org/2026/07/20/rogallo-v0-12-0.html
```

To be clear: this isn't intended to be a serious finger command (like, why
would anyone even need that?), it's just a tool within the library that can
be used to do some testing within a development (v)environment.

At some point soon I'll be adding `port79` as a dependency of Rogallo and
adding `finger` as a "native protocol".

[//]: # (2026-07-21-port79-a-finger-protocol-library-for-python.md ends here)
