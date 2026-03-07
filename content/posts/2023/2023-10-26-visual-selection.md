---
layout: post
title: Visual Selection
category: Coding
tags: Python, evolution, biology, terminal, textual
date: 2023-10-26 18:50:00 +0100
cover: attachments/2023/10/26/visual-selection-cover.png
---

Over the last few weeks I've had a couple of sessions of working on a
library to wrap [Plotext](https://pypi.org/project/plotext/) -- a popular
terminal-based plotting library for Python -- so that it can easily be used
in Textual apps;
[`textual-plotext`](https://textual.textualize.io/blog/2023/10/04/announcing-textual-plotext/)
is the result.

I feel it's come together pretty well

But... I've been itching to find a reason to use it in a project of my own.

Meanwhile...

Back in the mid-2000s, when [phpBB](https://en.wikipedia.org/wiki/PhpBB)
systems were still the fashion, I used to hang out on a site that was
chiefly aimed at the atheist and secular humanist crowd. We'd get a good
number of drive-by
[YEC](https://en.wikipedia.org/wiki/Young_Earth_creationism) types who'd
want to argue (sorry... debate) and often talk nonsense about biology and
the like.

Now, I'm no biologist, I'm no scientist, I'm just a hacker who likes to
write code for fun and profit; so any time there was a chance to write some
code to help illustrate an idea I'd jump at the chance. I forget the detail
now -- this was back in 2008; 15 years ago as of the time of writing -- but
one time I remember a conversation was taking place where someone was just
flat out claiming that "random mutation" can only cause "loss of
information" and could never lead to a "desired result", or some such thing.

If you've ever had, read or watched those debates, you'll know the sort of
thing I mean.

So that got me thinking back then, could I write something that could give a
simple illustration of how this doesn't quite make sense?

So I had a little hacking session and came up with some Ruby code[^1] that
did what I felt was the job. You'd give it a phrase you wanted it to
generate (a stand-in for the current "fitness landscape", in effect), it
would then generate a totally random string of that length, and then would
set about mutating it, finding mutations that were "fitter" than others (a
stand in for selection), breed the best two so far (randomly copy one chunk
from another to create a child), then repeat over and over.

When I first wrote it I wasn't sure what to expect; would it ever finish
given a reasonably large target string?

It did.

It was fun to code.

It got posted to the BB and of course wasn't in any way persuasive to them
(honestly I never expected it would be). I seem to recall it being
hand-waved away with calls of there obviously being an intelligent designer
involved[^2].

Anyway, the "meanwhile..." in this: a few times this year I've thought it
could be fun to rework this in Python (it's really not that complex after
all; just a string-chopping loop really) and use Textual to put a fun UI on
it.

So, that's what I did, complete with `textual-plotext` plot:

![Visual Selection in action](/attachments/2023/10/26/visual-selection.png)

While, 15 years on, this isn't going to convince anyone of the underlying
point, I think it does serve a good educational purpose. It shows that you
can create a fun UI for the terminal, with Textual, with not a lot of code.
It also shows off how you can easily create dynamic plots. Plus -- and I
think this might be the really important one -- it shows you can write
"traditional" tight-loop code in a Textual application and *still* have a
responsive UI; all thanks to the [worker
API](https://textual.textualize.io/guide/workers/).

The heart of the code for this application is this:

```python
environment = Environment("This is the target string we want to create!")
while not environment.best_fit_found:
    environment.shit_happens()
```

Sure, there's some detail in the `Environment` class, but you get the idea:
while we've not hit the target, let [life find a
way](https://www.youtube.com/watch?v=kiVVzxoPTtg). A loop like that would
totally bog down an application with a UI without some other work taking
place. With Textual and workers the resulting method in the application,
complete with code to send updates to the UI, really doesn't look much
different:

```python
@work(thread=True, exclusive=True)
def run_world(self, target: str) -> None:
    worker = get_current_worker()
    environment = Environment(target)
    iterations = 0
    self.post_message(self.WorldUpdate(environment, iterations, *environment.best))
    while not worker.is_cancelled and not environment.best_fit_found:
        environment.shit_happens()
        iterations += 1
        if (iterations % 1000) == 0 or environment.best_fit_found:
            self.post_message(
                self.WorldUpdate(environment, iterations, *environment.best)
            )
    if environment.best_fit_found:
        self.post_message(self.Finished(iterations))
```

I honestly think the worker API is one of the coolest things added to
Textual and I so often see people have real *"woah!"* moments when they get
to grips with it.

Anyway... I've covered science, religion, and how Ruby is better than
Python, so I'm sure I've annoyed almost everyone. Job done I guess. ;-)

If you want to check out the app itself there's [a GitHub
repo](https://github.com/davep/visual-selection) and it can also be
installed [from PyPi](https://pypi.org/project/visual-selection/) using
`pipx`.

Expect it to be my tinker project of choice for a wee while; there's a
couple of other things I'd like to add to it.

[^1]: Possibly unpopular opinion with some folk who will read this, but I've
    long been a fan of Ruby as a language and actually generally prefer it
    to Python.
[^2]: Me, the coder. While utterly missing the point of a simple
    illustration, while apparently not understanding the concept of an
    analogy, I guess at least they felt I was intelligent?

[//]: # (2023-10-26-visual-selection.md ends here)
