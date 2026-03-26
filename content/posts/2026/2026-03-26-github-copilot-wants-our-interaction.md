---
title: GitHub Copilot wants our interaction data
date: 2026-03-26 08:42:37+0000
category: AI
tags: AI, Coding, Copilot, Free Software, GitHub
cover: /attachments/2026/03/26/thumbs-down.png
---

I guess it was inevitable[^1], but yesterday GitHub
[announced](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)
a new opt-out approach to learning from people's interactions with
[Copilot](/tag/copilot/). I don't have anything novel or insightful to say
on this switch, and I'm sure folk with better-informed opinions have already
rushed out posts and articles about this, but I did want to jot down just
how curious I am to see this roll out.

For starters: for me this feels like one of those things that will get a lot
of backlash, and in a day or so GitHub will say they're pausing rolling this
out while they reevaluate this approach[^2]. Then, eventually, they roll it
out anyway after a "period of consultation with the community". That sort of
thing.

I've not read further this morning, but before going to bed last night it
wasn't a happy time in the comments section of [the
FAQ](https://github.com/orgs/community/discussions/188488). I can also see
why some would be cynical about this change, given the tone of some of the
questions and answers in that FAQ. I'll hand it to them: they're pretty
candid and honest with the FAQs, but kinda yikes too.

![A bad time in the FAQ](/attachments/2026/03/26/thumbs-down.png#centre)

Here's the key thing I'm curious about, and which I'll be thinking about and
watching for movement on in the next few days: all the talk here seems to be
about protecting the privacy of the proprietary code of businesses[^3].
That... is understandable, from a business point of view, from a commercial
adoption point of view, from a *"we want all software engineering
departments to use Copilot"* point of view. But how the heck are they
*really* going to manage that?

In the comments in the FAQ [this explanation stood
out](https://github.com/orgs/community/discussions/188488#discussioncomment-16317873):

> We do not train on the contents from any paid organization’s repos,
> regardless of whether a user is working in that repo with a Copilot Free,
> Pro, or Pro+ subscription. If a user’s GitHub account is a member of or
> outside collaborator with a paid organization, we exclude their
> interaction data from model training.

This seems somewhat unclear to me. Let's walk this one through for a moment:
[my GitHub account](https://github.com/davep) *is* a member of a "paid
organisation". My account is also my account, for my personal code, I've had
it [a long time](/2023/10/01/all-green-on-github.html) and it's filled with
a lot of FOSS repos and I keep adding more. So which scenario is the right
one here?

1. Because I'm currently a member of at least one "paid organisation" I'm
   always opted-out of this training no matter how the opt in/out setting is
   set and no matter what code I work on?
2. Because I'm currently a member of at least one "paid organisation" I
   *can* opt in when working on code that is from a repository which is
   mine, but I'm opted out when I'm working on code from a repository
   belonging to the paid organisation?

I think it reads like it's #1. But then that seems rather odd to me because,
if I go and look at my settings right now, I can elect to opt in/out of this
training system. If the correct reading is #1 why not just disable that
setting altogether and say below it that I'm opted-out because I'm part of a
paid organisation?

Which sort of suggests we should perhaps read it as #2? If that, that raises
all sorts of questions. How would Copilot know I'm working on code from such
a repository? Sure, it's not impossible to infer if I am working within the
context of a given repository, doing some fun stuff to work out the origin
and so on, but it feels messy. It also feels like a scenario that could end
up being incredibly leaky. It really would not be difficult to run into a
scenario where I'm working on some [non-Free
code](https://www.gnu.org/philosophy/categories.html) but in an environment
where the licence isn't clear, or where it appears that the licence[^4]
would permit such training.

Or... perhaps there's a #3, or a #4, or so on, that I've not even considered
yet. The fact that software engineering departments suddenly have to start
thinking about this issue (yes, I know, it's been a background issue for a
while but this really drags it out into the open) is going to make for a few
interesting weeks, assuming people care about where their code ends up.

Who knows. Perhaps, in some strange way, this *is* how all software ends up
being [Free](https://www.gnu.org/philosophy/free-sw.html).

[^1]: And I think a bit of me is surprised that they weren't just doing it
    anyway.
[^2]: This isn't a prediction, I'm just saying it feels like that sort of
    announcement.
[^3]: It's not that simple, but to save getting into the deep detail...
[^4]: I'm using licence here as shorthand for a lot of things to consider
    relating to who should have access to the code and how.

[//]: # (2026-03-26-github-copilot-wants-our-interaction.md ends here)
