---
title: "Gemini client history (redux)"
date: "2026-06-22 19:47:06+0100"
category: Coding
tags: [Coding, "Gemini Protocol", Hike, Python, Rogallo, smolweb, textual]
cover: "/attachments/2026/06/22/gemini-client-with-history.webp"
---

A couple of days ago [I thought I had history working well in the Gemini
client I'm working on](/2026/06/20/gemini-client-history.html); I was wrong.
It worked, but the more I used it the more I felt it wasn't quite right. The
main problem was I had a single history structure that served both the
navigation history (moving backwards and forwards) as well as the general
location visit history (the list of places I've visited). It made sense
initially, but in use it just wasn't cutting it.

So now I've redone it, using two different history lists that also grow in
rather different ways. For the navigation history, when "adding" a new
location, everything after the current location gets removed, making the new
location the latest in the list. The visit history, on the other hand, grows
more like an ordered set: if I add a location that is already in the list,
the older version is removed and it is added to the end of the list. In
doing this, it's also allowed me to track the date and time I've visited a
location, which means I can now have a useful history panel (which can be
popped in and out of view) that shows me where I've been, and when.

![Client, showing the history panel](/attachments/2026/06/22/gemini-client-with-history.webp#centre)

Having done this, I now want to take some of these approaches and apply them
to [Hike](https://hike.davep.dev/). It has a pretty simple location and
navigation history system that suffers from the same issues that I wasn't
liking in this project. It'll benefit quite a bit from this improvement. I
sense a v2.0.0 of Hike in the next few months.

As for when I'll let *this* project see the light of day: I think I'm close
to opening the repository and publishing the first version to
[PyPI](/tag/pypi/). I had wanted to do it sometime yesterday, but the above
kicked in and I've been tinkering more to try and make a stable foundation
for the initial release. There's still a lot of work needed for it to be
feature-complete, but there's enough here to play and experiment.

[//]: # (2026-06-22-gemini-client-history-redux.md ends here)
