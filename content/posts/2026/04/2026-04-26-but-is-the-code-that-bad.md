---
title: But is the code that bad?
date: 2026-04-26 09:29:49+0100
category: AI
tags: AI, Coding, Copilot, Gemini, Google, Python, code review
---

There is, obviously and understandably, a *lot* of conversation online about
AI and coding and agents and all that stuff. Much of it I get, much of it I
agree with, I share the vast majority of the concerns. The impact on people,
the impact on society, the impact on the environment, the impact on
security... there's a good list of things to worry us there.

The one that crops up a lot though, that I don't quite get, is the constant
claim I see that at best AI tools produce bad code, and at worst they
produce unworkable code. That really isn't my recent experience.

Sure, going back to 2023 or 2024, when I first started toying with these new
chatbot things some folks were raving about, the output was laughable. I can
remember spending some fun times trying to coax whatever version of ChatGPT
was on the go at the time into writing workable code and being amused by
just how bad it was.

Even back in October last year, when I first tried out the free
[Copilot](/tag/copilot/) Pro that GitHub had given me to play with, I tried
to get it to build a [Textual](/tag/textual/) application for me and it was
terrible. The code was bad, it didn't really know how to use Textual
properly, the application I was trying to get it to write as a test barely
worked. It was a disaster.

A month later, in November of last year, I had a second go and better
success. That time the (still not released, perhaps one day) application I
was building was [Swift](/tag/swift/)-based and worked really well, but I
can't really comment on the quality of the code or how idiomatically correct
the code is in respect to the type of application it is (it's a wee game
that runs on iOS, iPadOS, macOS).

By the time I [tried my first serious
experiment](/2026/02/20/five-days-with-copilot.html) things seemed to be a
little different. The code actually wasn't bad. It wasn't good, it was *far*
from good, but it wasn't bad. Also, because it was Python, I was in a good
place to judge the code.

Since I've started working on [BlogMore](https://blogmore.davep.dev/) I've
noticed issues such as:

- Lots of repetitive boilerplate code.
- Lots of magic numbers.
- Lots of magic strings.
- Functions with redundant and unused parameters.
- A default state of just adding more and more code to one file.
- A habit of writing least-effort-possible type hints.
- A habit of sometimes taking a hacky shortcut to solve a problem.
- A habit of sometimes over-engineering a solution to a problem.
- A weird obsession with `import`ing *inside* functions.
- An occasional weird obsession with guarding some imports with
  `TYPE_CHECKING` to work around non-existent circular imports.
- An unwillingness to use newer Python capabilities (I've yet to see it make
  use of `:=` without being prompted, for example).
- A tendency to write what I would consider less-elegant code over
  more-elegant code.

The list isn't exhaustive, of course. The point here is that, as I've
reviewed the PRs[^1], and read the code, I've seen things I wouldn't
personally do. I've seen things I wouldn't personally write, I've seen
things I've felt the need to push back on, I've seen things I've fully
rejected and started over. Ultimately BlogMore isn't the code I would have
written, but at the moment it is the *application* I would have written[^2].

So, here's the thing: every time I see someone writing a negative toot or
post or article or whatever, and they talk about how the code it produces is
unworkable, I find myself wondering about how they formed this opinion. Are
they just writing the piece for the audience they want? Are they writing the
piece based on their experience from months to years back, when these tools
did seem to still be laughably bad? Are they simply cynically generating the
piece using an LLM to bait for engagement? When I see this particular aspect
of such a post it's a bit of a red flag about where they're coming from,
kind of like how you suddenly realise that someone who seems to speak with
authority might be full of shit when they start to spout questionable
"facts" on a subject you understand well.

But wait! What about that list of dodgy stuff I've seen while building
BlogMore with Copilot? What about all the reading and reviewing I've had to
do, and what about the other crimes against Python coding I can probably
still find [in the codebase](https://github.com/davep/blogmore)? Surely that
is evidence that these tools produce terrible, unworkable, unusable code?

I mean, okay, I suppose I could reach that conclusion if I'd had a massively
atypical experience in the software development industry and had never had
to review anyone else's code, or had never needed to work on someone else's
legacy code. Is what I'm seeing out of Copilot something I'd consider ideal
code? Of course not. Is it worse than some of the worst code I've had to
deal with since I started coding for a living in 1989? Hell no!

From what I'm seeing right now I'm getting code whose quality is... fine.
Mostly it does the job fine. Often it needs a bit of coaxing in the right
direction. Sometimes it gets totally confused and goes down a rabbit hole
which needs to just be blocked off and we start again. Occasionally it needs
rewriting to do the same thing but in a more maintainable way.

All of which sounds very familiar. I've had times where that describes *my*
code (and I would massively distrust anyone who says they've never had the
same outcomes in their time writing code). For sure it describes code I've
had to take over, maintain or review.

It's almost like it was trained on lots of code written by humans.

Meanwhile... not every instance of using these tools to get code done needs
to be about writing actual code. More and more I'm finding Google Gemini
(for example) to be a really handy coding buddy and faster "Google this shit
'cos I can't remember this exact thing I want to achieve". I'll ask, I'll
almost always get a pretty good answer, and then I can generally take that
snippet of code and implement it how *I* want.

I've seldom had to walk away from that sort of interaction because it was
getting me nowhere.

All of which is to say: I remain concerned about a great many things in the
AI space at the moment, but I'm also as equally suspicious of someone who
just flatly says *"and the code it produces just doesn't work"*. If that's
part of an article or post I'm left with the feeling that the author put
zero actual effort into forming their opinion, let alone actually writing
it.

[^1]: To varying degrees. Sometimes I have plenty of time to kill and I read
    the PR carefully, other times I glance it over, be happy there's nothing
    horrific there, and then decide to push back or merge based on the
    results of hand-testing and automated testing.
[^2]: To be fair, it's the application I would still be writing and would be
    some time off finishing; there's no way it would be as feature-complete
    as it is now had I been 100% hand-coding it.

[//]: # (2026-04-26-but-is-the-code-that-bad.md ends here)
