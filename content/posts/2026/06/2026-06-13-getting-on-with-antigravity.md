---
title: "Getting on with Antigravity"
date: "2026-06-13 16:47:26+0100"
category: AI
tags: [Antigravity, Coding, Gemini, Google]
cover: "/attachments/2026/06/13/ag-quotas.webp"
series: ["Agentic Afterthoughts"]
---

It's been a wee while now since I [stopped using GitHub
Copilot](/series/the-great-github-copilot-meltdown-of-2026/) and switched to
doing everything locally (in a tool sense, not a model sense) with the
[Antigravity](/tag/antigravity/) CLI, so I thought I'd jot down how it's
been going. Simply put, it's been going well.

I've found the CLI itself easy enough to work with (I've not really
attempted to use the GUI application), and the default model choice has done
a lot of work for me on [BlogMore](https://blogmore.davep.dev/) without
issue. I think it's fair to say that, at this point, I'm finding it
far more consistent than I was finding Copilot+Claude.

As for the [initial confusion and concerns about
quotas](/2026/05/26/still-confused-about-antigravity-quotas.html): I've
found that that's calmed down, with me never obviously coming close to
hitting my limit while working on any change to BlogMore. The worst I've
seen is getting down to about 20% of the 5-hour rolling window, and even
then that's been when I've pretty much finished the work I was doing.

The actual display of quotas has changed too, I noticed just this morning.
Now, rather than showing progress bars per model, it's more like this:

![The new Antigravity quota display](/attachments/2026/06/13/ag-quotas.webp#centre)

While I suspect the weekly quota display will cause a smidge of anxiety to
start with, mostly I appreciate that being added, and being so clear. Given
the level of work I'm using this for, I can't see myself coming close to
using it all up and having to wait. The quota does come with an explanation
in the CLI too:

> Within each group, models share a weekly limit and a 5-hour limit. Quota
> is consumed proportionally to the cost of the tokens. Thus, limits will
> last longer with shorter tasks or using more cost-effective models. The
> 5-hour limit smooths out aggregate demand to fairly distribute global
> capacity across all users, while your weekly limit is tied directly to
> your individual tier.

Digging a little deeper, I see there's a `/credits` command and, quite
quickly, I can go from that to this in my browser:

![I can buy more credits](/attachments/2026/06/13/buy-credits.webp#centre)

I'm not sure exactly how much work 2,500 credits might represent, or what
impact it would have or could have on the weekly quota; confusingly, if I
follow the links from the CLI to see my usage, I see a message that says:

> AI credits included with your plan have been replaced by product-based
> usage limits

So which is it? Do I have usage limits? Do I have a hard cap for a week? Can
I extend it or not? Do I extend it using credits or not? I sense the
messaging around this is all still a little mixed up. I do know that if I
turn on credit fallback in `/settings`, I get a handy display of the credits
I have left:

> AI Credits: 1000

So this weirdly reads like I can and am using credits as a fallback to the
quota, but also not.

Schrödinger’s Quota?

I'll dig around some more and see if I can find a definitive answer.

All that said: barring any changes that might upset things (which, let's be
honest, is something that's highly likely given the state of the AI/agentic
coding world), I think I'm happy with how this is going. For now, at least,
BlogMore's primary development tool will carry on being Antigravity.

And me, of course.

[//]: # (2026-06-13-getting-on-with-antigravity.md ends here)
