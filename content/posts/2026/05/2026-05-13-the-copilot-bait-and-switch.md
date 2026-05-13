---
title: The Copilot bait and switch
date: 2026-05-13 08:31:27+0100
category: AI
tags: AI, Business, Copilot, GitHub
cover: /attachments/2026/05/13/the-new-price.webp
---

Well, it's here: GitHub's tool to let you see how much better off you're
going to be under the new Copilot billing system that comes in next month.
It's... something.

But let's set the background first. I'm here (in [Copilot](/tag/copilot/)
usage space) as an observer, spending time on an experiment that started
with the free pro tier and then transitioned into the *"okay, I'll play
along for $10 a month, the [tool I'm building is fun to work on and is
useful to me](https://blogmore.davep.dev/)"* phase. I doubted it would last
forever -- the price was obviously too good to be true for too long -- but I
wasn't expecting it to collapse quite so soon and in quite such a
spectacular way.

When GitHub [announced the move to usage-based
billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)
I was curious to see if I'd be better off or worse off. It was hard to call
really. My use of Copilot is sporadic, and as BlogMore has started to settle
down and reach a state approaching feature-saturation the need to do heavy
work on it has reduced. I did use it a fair bit last month, but that was
more in tinkering and experimenting mode rather than full development
mode[^1], so it's probably a good measure.

Checking the details on GitHub, it looks like I used a touch under 1/3 of my
premium requests.

![A table of my premium requests for April 2026](/attachments/2026/05/13/requests-table.webp#centre)

It also looks like the usage came in a couple of bursts lasting a few days,
with a pretty flat period in the middle of the month.

![Cumulative use for April](/attachments/2026/05/13/april-usage.webp#centre)

So, technically, GitHub won. I paid them $10 for 300 premium requests, I
left a touch over 2/3 unused. I think it's fair to suggest that I'm a pretty
lightweight user, even when I have a project under active development.

This is where the new usage-based preview tool comes in. Launched yesterday,
it lets you take your existing usage stats and see how much it would have
*really* cost you.

The app itself comes over as being hastily spat out with an agent and little
communication between responsible teams. You'd *think* you just press a
button when viewing some historical usage figures and get a display that
shows you what it would cost under the new approach.

You'd think.

Nope. First you generate your report for a particular month. Then have to
ask for it to be **emailed to you as a CSV**!

![Requesting the email](/attachments/2026/05/13/email-report.webp#centre)

Even that part isn't super reliable. When I tried it last night it took a
wee while to turn up, and that was after about 10 attempts where I got an
error message saying it couldn't generate the report. This morning I tried
again and I've yet to see the email, 30 minutes later[^2].

Having done that you click through to another page/app where you have to
upload the CSV, to GitHub, that GitHub just sent you in an email. Brilliant.
It then gives you the good news.

So what is my 1/3 use of the premium request allowance going to save me
under the new approach to billing?

![Such a good deal](/attachments/2026/05/13/the-new-price.webp#centre)

Amazing. I especially like the part where they spin it as: if I spent
$39/month with them I would save money!

I guess I should take comfort that I'm not [that one Reddit user whose $39
April would really have cost them almost
$6,000](https://www.reddit.com/r/GithubCopilot/comments/1tbfkui/ill_just_leave_this_here/)[^3].

Watching this journey has been wild. The free Pro as a taster to get me onto
$10/month I can go with, that's fair enough. For the longest time I never
even paid it any attention. But watching GitHub give it to so many people,
and especially so many students, and then watching them do *shocked Pikachu*
when it cost them an arm and a leg and probably caused the degradation of
the performance of their systems... who could possibly have seen this
coming? [Impossible to
predict](https://en.wikipedia.org/wiki/Tragedy_of_the_commons).

Back when I first wrote about my initial impressions of working with Copilot
I wondered [in the
conclusion](/2026/02/20/five-days-with-copilot.html#conclusion) if I'd
transition to a paying version of Copilot. I obviously did. At $10/month it
was a very affordable tinker toy that gave me a new dimension to the hobby
side of my love of creating things with code. But the prospect of paying
$39/month for something in the region of 1/3 of requests that I had before:
nah, I'm not into that.

It looks like this month will be the last month I keep a Copilot
subscription. BlogMore will carry on being developed, I'll probably
transition to leaning on [Gemini](/tag/gemini/) CLI more ([as I have been
the last week anyway](/2026/05/11/speeding-up-blogmore.html)), and also
start to get my hands dirty with the code more too.

This feels like one of the early signs of the bait and switch that the AI
suppliers have been building up all along. Experimenting and better
understanding how and why people use these tools has been seriously useful,
and I can't help but feel that I accidentally started at just the right
moment. Watching this happen, with actual experience of what's going on, is
very educational. It's going to be super interesting to see if this same
stunt gets pulled on a bigger scale, with all the companies that
uncritically embraced AI at every level of their organisation.

It's going to be especially interesting to watch the AI leaders in those
companies to see how they spin this, if and when the real costs are more
widely applied.

[^1]: Is my recollection. I should probably [review the
    ChangeLog](https://blogmore.davep.dev/changelog/) and see what I
    actually did add in April.
[^2]: Yes I checked spam.
[^3]: In part because yikes, but also in part because at least I'm not the
    reason this is happening, unlike them.

[//]: # (2026-05-13-the-copilot-bait-and-switch.md ends here)
