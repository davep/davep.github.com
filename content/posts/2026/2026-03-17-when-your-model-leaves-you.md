---
layout: post
title: When your model leaves you
category: AI
tags: Python, Blogging, AI, LLM, Copilot, GitHub, BlogMore
date: 2026-03-17 10:00:00 +0000
cover: /attachments/2026/03/17/copilot-models.png
---

Yesterday evening, after dinner, but just before [loading up a game released
just a few hours
earlier](https://store.playstation.com/en-gb/concept/10016557), I decided to
kick off a change to [BlogMore](https://blogmore.davep.dev/). Part of the
[ongoing experiment](/2026/02/20/five-days-with-copilot.html) is this
convenience aspect: where I can get some work going and then go and do
[something entirely different](https://www.youtube.com/live/tIqDQucBf5U).

The nature of the change itself isn't important (I'll write about it when I
release an update), but something that happened is. As usual, I did the
prompt as an issue, and assigned it to [Copilot](/tag/copilot.html). The
first thing that was curious was that, after around 5 minutes, despite it
having added the 👀 reaction (which it seems to use to indicate the agent
has seen it has work to do), nothing happened. I didn't see an agent kick
off doing the work. Eventually I gave up waiting and opened a Copilot
session and asked it to set about dealing with the issue I'd raised.

It did as I requested, but apparently alongside another agent which had
suddenly started doing the exact same work. Thinking it was a glitch (it's
not like GitHub hasn't been [having some trouble of
late](https://github.blog/news-insights/company-news/addressing-githubs-recent-availability-issues-2/))
I stopped the newest one and let the "original" go about its work.

A wee bit later, just before I started up my game and the stream, I checked
in on how it was doing. It had finished, but in a quick test, I noticed a
small bug. I [prompted it to fix the
problem](https://github.com/davep/blogmore/pull/304#issuecomment-4069988596),
closed the tab, and went about the real business of killing bugs.

Fast forward a couple of hours, I was done with getting my arse kicked on
Klendathu, I packed away my controller and headset and opened GitHub again
to see where Copilot was at. [It wasn't
good](https://github.com/davep/blogmore/pull/304#issuecomment-4069988954):

> @davep The model `claude-sonnet-4.6` is not available for your account.
> This can happen if the model was disabled by your organization's policy or
> if your Copilot plan doesn't include access to it.
>
> You can try again without specifying a model (just `@copilot`) to use the
> default, or choose a different model from the model picker.
>
> If you want to contact GitHub about this error, please mention the
> following identifier so they can better serve you:
> `79b81d32-e26a-4898-bd41-4bba088d08f6`
>
> <!-- copilot-coding-agent-error: model-not-available -->

Wait... what? I've been using this for weeks now, as best as I can tell I've
generally been making all the changes and improvements using Claude Sonnet
4.6; there's never been an issue. Then, suddenly, in the middle of a PR, I
don't have it?

Quickly checking elsewhere, sure enough, I had access to almost no models. I
can't remember what there was, but it wasn't much and *all* the Claude ones
had disappeared. Even if I tested in the [Copilot
CLI](https://github.com/features/copilot/cli)[^1] I saw a very limited set
of models.

Around this time I had two reactions: one was something like *"cool, this is
an important part of the experiment, knowing how it goes if your models are
taken from you"*, the other was a curious *"but Claude and I have an
understanding about this codebase I can't trust some other model I've not
been using"*.

As it was getting late into the evening and I still wanted to watch an
episode of Stargate SG-1 (yes, I'm doing a full rewatch given it's on
Netflix) I closed the MacBook and decided to check in on the issue in the
morning.

Fast forward [one SG1 episode](https://www.imdb.com/title/tt0709091/) later
and, just before I headed to bed, I decided to do a quick search. While it
could be a problem with my own account, it felt like it was more of a
general issue. [It was more of a general
issue](https://github.com/orgs/community/discussions/189795). At that point
(around 23:20 UTC), checking in the GitHub app on my phone, I could see that
some, if not all, of the models I was used to seeing, had come back.

As of this morning, as of time of writing, it's all looking back to how it
was.

![All the models back](/attachments/2026/03/17/copilot-models.png)

All of which is a great reminder, and something useful in the experiment:
what *does* happen when some third party takes away the models you're using
to get your work done? In the time I've been building up BlogMore I've come
to trust the quality of Claude Sonnet (in the sense that I know when and
where I have to pay closer attention to what it's done, and where it'll very
likely have done a pretty good job[^2]), so finding that I'd possibly have
to switch to some other model that I've had no experience with... I
genuinely had a moment of concern about how and where I was going to take
BlogMore.

Ultimately it's not *actually* a serious concern for me: while I aim to
maintain it for a very long time to come (it is how I'm creating the site
for this blog after all), BlogMore isn't that critical. Moreover, I know I
could cease using Copilot to create and maintain it and I could tidy up the
code and hand-update and hand-manage it. There's a reason why I decided to
really dive into this using a language I'm extremely confident with.

But for those applications some might now be relying on, developed by
someone keen but as yet unskilled, what way forward for them if [such a
situation were to happen and not be
resolved](https://github.com/orgs/community/discussions/189268)?

[^1]: Which I'm not really using at the moment, but do have installed to
    experiment with.
[^2]: So just like working with humans, oddly enough.

[//]: # (2026-03-17-when-your-model-leaves-you.md ends here)
