---
layout: post
title: Textual Query Sandbox Update
category: Python
tags: PyPi, Python, coding, Textual
date: 2023-09-10 09:22:00 +0100
cover: attachments/2023/09/10/tqs-1.png
---

Since [quickly hacking together `textual-query-sandbox` a few days
back](/2023/09/01/textual-query-sandbox.html), I've made a bunch of small
changes here and there. While most have been cosmetic and playing with some
ideas, some have also been internal improvements that should make the tool
work better.

The most prominent change is one I pondered in the previous post, where I
thought it might be interesting to have a small collection of playgrounds
grounded together with a `TabbedContent`. So as of now the tool still has
the original playground which had an emphasis on nested containers:

![Playground 1](/attachments/2023/09/10/tqs-1.png#centre)

There's now a playground with an emphasis on selecting widgets within
containers[^1]:

![Playground 2](/attachments/2023/09/10/tqs-2.png#centre)

There's also now a playground that has an emphasis on pulling out widgets
based on ID and classes:

![Playground 3](/attachments/2023/09/10/tqs-3.png#centre)

The other change you will notice from the original post is the DOM tree
shown in the bottom right corner. Note that that isn't there to show your
query result (that's the bottom left panel), it's there to help picture how
the DOM in the current playground hangs together, and will hopefully help in
picturing the structure for when you write a query.

I sense there's still a lot of fun things I could add to this, and I'm still
keen on the idea of having the playgrounds "soft coded" in some way, so
people can make their own and load them up.

Another thing I want to try and work on is making the display as useful as
possible. While I think it's actually pretty neat and clear, there's not a
*lot* of space[^2] available to show the playground and the results. Finding
a good balance is an interesting problem.

For a number of reasons this is turning into a really enjoyable tinker
project.

[^1]: This is, of course, slightly nonsensical wording. Containers *are*
    widgets in Textual. Pretty much everything you see in your terminal is a
    widget, even a `Screen` is a widget.
[^2]: A lot of this of course hinges on how big someone's terminal is. I
    tend to run a fairly high resolutions with the smallest font I find
    readable so my terminal windows are often pretty "big"; other people
    tend to have something much smaller in terms of cell with/height.

[//]: # (2023-09-10-textual-query-sandbox-update.md ends here)
