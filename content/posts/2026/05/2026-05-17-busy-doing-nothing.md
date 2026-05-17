---
title: Busy doing nothing
date: 2026-05-17 10:08:03+0100
category: AI
tags: AI, Coding, Gemini, Google
---

The first company I worked for full-time had two offices. One in the south
of England, another in the north. Despite being a northern lad, I'd somehow
found myself working in the southern office. While the company used a few
languages, there was a split between the two offices, mostly driven by the
fact that the northern office was more minicomputer-based (lots of DEC stuff
as I recall), whereas at our office it was more PC-based (we were an
[Apricot](https://en.wikipedia.org/wiki/Apricot_Computers) dealership,
amongst other things). At our office, the predominant language was
[Clipper](https://en.wikipedia.org/wiki/Clipper_(programming_language))
(later to be called CA-Clipper).

At one point, at the other office, they hired someone to start doing Clipper
coding up there too, and he was handed his first project, to add a new
report to an existing system. After around three weeks, he just didn't turn
up for work one day, called in to say he'd quit (or so I was told).
Meanwhile, the work he had done didn't seem to be working. If someone took
the newly-compiled system and ran the new report, nothing happened.

When the code was looked at, it became clear why. The new module had one
line of code. Well, not one line of code exactly: it had a one-line comment.

```clipper
* This is too hard. I can't do this.
```

That was it. He'd spent those weeks appearing to work on the requirement,
but never produced a single line of actual code.

I felt really bad for the guy. He'd somehow managed to make it through the
interview, somehow managed to convince others, and himself, that he was
capable of working with Clipper and writing code (probably made easier by
the fact that the office in question wasn't a "Clipper shop"). But when it
came to actually getting on with a job, he'd been unable to get it done
(and, apparently, had felt unable to ask anyone around him for help, which
probably says a lot about that office and the industry at the time[^1]).

I bring this up because I was reminded of this story when I was tinkering
with [Gemini](/tag/gemini/) last night. While working on the [optimised
images PR](https://github.com/davep/blogmore/pull/492), towards the end of
the session, I asked it to make a particular change. It then started
"thinking", and after a couple of minutes appeared to get to work on the
problem. It kept printing, scrubbing out and printing again, lines of text
of what it was apparently doing. This went on for something like five
minutes. Eventually it announced that the work had been done, explained what
it had changed, and how it had implemented the requirement.

I flipped to another terminal to test out the work and... no changes. Zero
changes. Nothing to diff, nothing to commit.

I flipped back to the CLI app, mentioned that nothing had changed, and it
then very quickly made some edits; nothing spectacular, a 14-line diff
affecting five lines (to start with).

This is the first time I've seen this, and I guess yet another thing I need
to keep an eye out for. Of course I would notice if I asked for some work to
be done and it wasn't done (I did), but it feels like another method via
which this "productivity tool" can make you less productive.

If you give me the under-qualified, solution-paralysed, entry-level
developer who doesn't know how to proceed, I can help them. Their current
inability to actually bash on the keyboard and make code appear isn't the
problem here. Giving them a tool that will busy-work for five minutes and
produce nothing isn't going to help them, neither will things improve if
they're given a tool that *does* emit all the code. Removing the human
element is going to remove safety, growth and also domain knowledge. I feel
it's going to rot software engineering departments from within, if handled
badly.

Watching people talk about agents as if they're the solution, and that
writing code is now a solved problem, really troubles me. I won't question
the idea that it can be a very useful tool -- goodness knows I've found it
useful recently -- but I do question the common assertion that it finally is
a [silver bullet](https://en.wikipedia.org/wiki/No_Silver_Bullet). I find
this to be lazy, dangerous and harmful thinking.

[^1]: Because of course we're so much better as an industry these days.

[//]: # (2026-05-17-busy-doing-nothing.md ends here)
