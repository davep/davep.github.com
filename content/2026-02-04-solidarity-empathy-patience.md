---
layout: post
title: Solidarity, Empathy, and Patience -- thinking about code reviews
category: Coding
tags: work, review, leadership, Death Stranding
date: 2026-02-04 13:50:00 +0000
cover: attachments/2026/02/04/chiral.jpeg
---

## So I saw this video...

![A chiral crystal](/attachments/2026/02/04/chiral.jpeg#centre)

Death Stranding, along with its sequel, is my absolute favourite video game
ever, and probably one of my favourite pieces of fiction ever too; I've
watched and read a lot about the game (not to mention I've [played both
releases a ton
too](https://www.youtube.com/playlist?list=PLUY2FpMDyORDJd_VYhF74e6Mapf8oHp8i)).
A good few months back I was watching [a video about the making of the first
game](https://youtu.be/_GhSXMMJp0E?si=dGxAJlgLi5BBKCkM) and during the
video, [around the 27:20
mark](https://youtu.be/_GhSXMMJp0E?si=z6FKH_FNfFMEozAe&t=1635), the narrator
says the phrase:

> the game's core values of solidarity, empathy, and patience

This stood out to me. There was something about that phrase and what it
meant given my experiences in Death Stranding and Death Stranding 2; it
spoke to me enough that I jotted it down and kept coming back to it and
thinking about it. It was a phrase I couldn't get out of my head.

Around the same time I was also doing a lot of thinking about, and
note-writing about, code reviews. Although I've been working in software
development[^1] for a few decades now (I started in July 1989), I was quite
late to the whole process of code review -- at least in the way we talk
about it today. This mostly comes down to the fact that for a lot of my time
I either worked in very small companies or I was the only developer around.

Given this, thinking about my own approach to reviews is something I've only
really been doing for the past few years. I've made personal notes about it,
read posts and articles about it, I've had conversations about it; my
thoughts and feelings about it have drifted a little but seem to have
settled.

The idea of that phrase from the Death Stranding video crept into this
thought process, as I felt it nicely summed up what a good code review would
look and feel like. Weirdly I also realised that, perhaps, the things I like
and value about Death Stranding are also the things I like, value, and want
to embody when it comes to code reviews.

One of the big selling points for me, with Death Stranding, is the
asynchronous multiplayer aspect of it; the reason Kojima calls it a "Strand
type game". I have my game, I have my goal, but other people can indirectly
affect it, either doing work in their game that leaks into mine in a
beneficial way, or by leaking into mine in a way that I have to clean up.
There's something really satisfying about this asynchronous collaboration.
That feels similar to the collective effort of working in a single
repository, each person working on their own branch or PR, sometimes in
tandem, sometimes in series, sometimes to the benefit of each other and
sometimes in ways that block each other.

But that's not the point here. There's a similarity if I think about it, but
I don't want to get too carried away on that line of thought. It's the
phrase from the video I care about; it's the approach of involving
solidarity, empathy and patience I want to think about more.

## Solidarity

![In the mountains](/attachments/2026/02/04/mountains.jpeg)

This, for me, is all about where you position yourself when you approach
reviewing code. I sense things only work well if you view the codebase as
something with common ownership. I've worked on and with a codebase where
the original author invited others in to collaborate, but where they
constantly acted as a gatekeeper, and often as a gatekeeper who was
resistant to their own contributions being reviewed, and it was an
exhausting experience.

I believe the key here is to work against a "your code" vs "my standard"
approach, instead concentrating on an "our repository" view. That's not to
say that there shouldn't be standards and that they shouldn't be maintained
-- there should be and they should be -- but more to say that they should be
agreed upon, mutually understood to be worthwhile, and that any callout of a
standard not being applied is seen as a good and helpful thing.

The driving force here should be the shared intent, and how the different
degrees of knowledge and experience can come together to express that
intent. If a reviewer can see issues with a submission, with a proposed
change or addition to the codebase, the ideal approach is to highlight them
in such a way as to make it feel like *we* discovered them, not that *I*
discovered them and *you* should sort it out. Depending on the degree of
proposed change, this might actually be expressed by (if you're using
GitHub, for example) using the "Suggested Change" feature to directly feed
back into the PR, or perhaps for something a little more complex, or the
offer to pair up to work on the solution.

## Empathy

![Sam and Fragile](/attachments/2026/02/04/Sam-and-Fragile.jpeg)

As someone who has written a lot of code, and so written a lot of bugs and
made a lot of bad design choices, I feel empathy is the easiest of the three
words to get behind and understand, but possibly the hardest one to actually
put into practice.

When you look at a PR, it's easy to see code, to see those design choices,
and to approach the reading as if you were the one who had written it,
assessing it through that lens. In my own experience, this is where I find
myself writing and re-writing my comments during a review. As much as
possible I try and ask the author *why* they've taken a particular approach.
It could be, perhaps, that I've simply missed a different perspective they
have. If that's the case I'll learn something about the code (and about
them); if that isn't the case I've invited them to have a second read of
their contribution. It seems to me that this benefits everyone.

I feel that where I land with this is the idea of striving to act less like
a critic and more like a collaborator, and in doing so aiming to add to an
atmosphere of psychological safety. Nobody should feel like there's a
penalty to getting something "wrong" in a contribution; they should ideally
feel like they've learnt a new "gotcha" to be mindful of in the future (both
as an author and a reviewer). Done right the whole team, and the work,
benefits.

## Patience

![Arriving at the plate gate](/attachments/2026/02/04/Plate-Gate.jpeg)

The patience aspect of this view of reviews, for me, covers a few things.
There's the patience that should be applied when reading over the code;
there's the patience that should be applied when walking someone through
feedback and suggestions; and there's the patience needed by the whole team
to not treat code reviews as a speed bump on the road to getting work over
the line. While patience applies to other facets of a review too, I think
these are the most important parts.

In a work environment I think it's the last point -- that of the team's
collective patience -- that is the most difficult to embody and protect.
Often we'll find ourselves in a wider environment that employs a myopic view
of progress and *getting things done*, where the burn-down chart for the
sprint is all that matters. In that sort of environment a code review can
often be seen, by some, as a frustrating hurdle to moving that little card
across that board. Cards over quality. Cards over sustainability.

It's my belief that this is one of those times where the phrase "slow down
to speed up" really does apply. For me, review time is where the team gets
to grow, to own the project, to own the code, to really apply the
development and engineering principles they want to embody. Time spent on a
review now will, in my experience, collectively save a lot more time later
on, as the team becomes more cohesive and increasingly employs a shared
intuition for what's right for the project.

## This is not (entirely) a post about code reviews

![Near the wind farm](/attachments/2026/02/04/Wind-Farm.jpeg)

The thing with code reviews, or any other team activities, is they don't
exist in a vacuum. They take on the taste and smell of the culture in which
they operate. It's my experience that it doesn't matter how much solidarity,
empathy or patience you display during your day-to-day, if it's counter to
the culture in which you work it's always going to be exhausting, it's
always going to feel like a slog.

If leadership in technology, in software engineering, were to show more of
these three basic qualities, they'd start to appear like they realise that
they're working with actual humans, not producers of code; and I think we
need more of that now than at any time in the history of coding.

Since I first saw that video, and heard that phrase, and had it run around
my head, I've come to feel that it's not just a good mantra for code
reviews; I think it's a simple blueprint for what good tech leadership
should look like. If there was more "Strand-type" leadership in my chosen
industry I feel it would be more open, more accessible, would offer more
psychological safety and ultimately would result in teams, and projects,
that thrive.

[^1]: Or software engineering, if you prefer, but that's a whole other blog
    post I'll never get round to writing one day.

[//]: # (2026-02-04-solidarity-empathy-patience.md ends here)
