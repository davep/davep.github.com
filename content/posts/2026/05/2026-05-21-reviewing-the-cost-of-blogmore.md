---
title: Reviewing the cost of BlogMore
date: 2026-05-21 16:51:18+0100
category: AI
tags: AI, BlogMore, Business, Copilot, GitHub, LLM
---

Now that we're near the end of the free or cheap [GitHub
Copilot](/tag/copilot/) party, I thought it might be interesting to look at
how much [BlogMore](https://blogmore.davep.dev/) has "cost" me to build, and
what it would have cost under the proposed new pricing structure that is
coming in next month. While I've [looked at the comparison for last
month](/2026/05/13/the-copilot-bait-and-switch.html), I've not looked at the
whole period I've been seriously using it.

So, for this review, I'm looking at all the data I can pull out of GitHub
for the months of February, March, April and May of this year. Development
of BlogMore [started back in
February](/2026/02/20/five-days-with-copilot.html) and, while it hasn't been
100% the cause of my use of Copilot premium requests, it's been almost all
of it. For the purposes of this review I'm just going to take the approach
that all I worked on was BlogMore.

Remember that, even when I had free access, I had a maximum of 300 premium
requests per month. Once I lost free access I had the same number of
requests for $10 a month.

Here's how those months broke down:

| Month      |       Paid | Premium Requests |    %age | Predicted Price |
|------------|-----------:|-----------------:|--------:|----------------:|
| February   |      $0.00 |              249 |     83% |          $21.67 |
| March      |     $10.00 |              140 |     47% |          $56.38 |
| April      |     $10.00 |              132 |     44% |          $53.77 |
| May        |     $10.00 |               34 |     11% |          $53.69 |
| **Total:** | **$30.00** |          **555** | **46%** |     **$185.51** |

So, give or take, something that I've actually spent $30.00 on could have,
at best, cost me $185.51. That's assuming that the "cost" of the models I
was using stays the same. You can see that the costs have risen already in
that the predicted price from February, where I used 83% of my premium
requests, is a touch under half the cost for this month, where I've used
just 11%. From what I can see in the raw data, it's down to some models
suddenly being considered more expensive (perhaps I was doing something that
just consumed more tokens, I'm not 100% sure if I'm honest, but I don't
recall anything that seemed like harder work).

Who knows what the real costs will be come June.

Now, technically, the actual cost under the new regime could or should be
$156, because it would be 4 lots of the $39.00/month plan, which would
better cover that use[^1]. Again though, that's assuming the actual cost of
using whatever models remains pretty stable. It also assumes that I'd want
to spend that much each month, and that I would be correctly anticipating
that I'd need that much.

Also, this isn't even the total cost of getting this project done. As I've
written recently: I've been using [Gemini CLI](/tag/gemini/) more this
month, and while the usage there is a flat cost, until now, [that's changing
too](/2026/05/20/the-gemini-bait-and-switch.html).

Now, of course, these aren't the only games in town. I could *"go to the
source"* and just get a sub for Claude Code or something, and as [Tim
pointed out over in the
Fediverse](https://mastodon.online/@xylophilist/116607946938312554),
something like [Cursor](https://cursor.com/) does a lot of this and is just
$20/month. Which all sounds fine, but what happens when those fleeing GitHub
Copilot or Gemini CLI/[Antigravity](/tag/antigravity/) head over to
something like Cursor? Is it sensible to expect the pricing to stay the
same[^2]?

I guess, at this point, I'm just mulling over the same issue time and again,
but from different angles. It does seem clear to me, though, that in less
than 4 months, in my experiment of *"what happens if I use agents to develop
a Free Software tool I want?"*, the market has gone from being entirely
reasonable to pretty much unjustifiable from a price point of view.

[^1]: As I understand it, the $39 gets you *almost twice* that value in "AI
    credits", so the [base allotment plus the flex
    allotment](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals#how-do-ai-credits-work)
    would cover what I've used.

[^2]: That's not even the main reason [to be concerned about a switch to
    Cursor](https://www.theguardian.com/technology/2026/apr/21/spacex-cursor-ai-startup).

[//]: # (2026-05-21-reviewing-the-cost-of-blogmore.md ends here)
