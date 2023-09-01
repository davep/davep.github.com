---
layout: post
title: Textual Query Sandbox
category: Python
tags: PyPi, Python, coding, Textual
date: 2023-09-01 07:42:00 +0100
---

Sometimes I can have an idea for a Textual widget, library or application on
my ideas list for weeks, months even, before I get around to it -- mostly
just due to not having the clear time to make a run at getting it going --
and then other times an idea can pop into my head and it *has* to be created
there and then. **Has** to be!

This happened yesterday evening.

While the tool I built is something I'd thought of before (back around
November last year I think) it hadn't even made it to my *"list of stuff I
should make"* that I keep in Apple Reminders; not sure why really. But then
yesterday evening a question cropped up on the [Textual Discord
server](https://discord.gg/Enf6Z3qhVr) that related to the subject and I was
reminded of it.

The subject being: [Textual DOM
queries](https://textual.textualize.io/guide/queries/). I like to think that
DOM queries in Textual are pretty easy to do, and well-explained in the
docs, but it's fair to admit that they need a bit of practice first, just
like any powerful tool. So I was reminded that I'd wanted to write a sandbox
application, that would have a practice DOM inside it, an input field to
type in a query, and a way of displaying the results.

So [`textual-sandbox-query`](https://github.com/davep/textual-query-sandbox)
was born!

![Textual Query Sandbox](/attachments/2023/09/01/tqs.png#centre)

In this very first version (which was *really* quickly put together -- it
was something like 15 minutes to write the main code and then probably 45
minutes tweaking styles, adding all the admin stuff to allow [deployment to
PyPi](https://pypi.org/project/textual-query-sandbox/) and writing the
README) there's an [`Input`](https://textual.textualize.io/widgets/input/),
a display of a group of nested containers with different IDs and classes,
and then a [`Pretty`](https://textual.textualize.io/widgets/pretty/) widget
at the bottom to show the
[`query`](https://textual.textualize.io/guide/queries/#query-objects)
result.

If you think this looks like it might be useful to you, it can be installed
using either `pip` or (ideally) `pipx`:

```sh
$ pipx install textual-query-sandbox
```

and then you can run it with:

```sh
$ tqs
```

At which point load up the Textual query docs, type queries into the input
field, hit enter and see what gets highlighted and which widgets end up in
the result set at the bottom of the screen.

Like I say: this was a quick hack yesterday evening, I think there's a lot
more can go into this. For one thing I think a more interesting practice DOM
would be a good idea, with a good mix of widgets; another thing could be
having a collection of different DOM playgrounds that can be switched
between (a `TabbedContent` of different playgrounds could be fun here); this
could even be taken further such that the user can create their own
playground DOM to practice against.

Eventually it would be neat if this could be turned into a library that can
be included in a Textual application, as a development-time debug tool, so
that on-the-fly test queries can be made.

For now though, it's started, it's under way, and I think the current
version probably covers 90% of the use cases for something like this; making
for a really quick and easy tool to double-check how to query something.

[//]: # (2023-09-01-textual-query-sandbox.md ends here)
