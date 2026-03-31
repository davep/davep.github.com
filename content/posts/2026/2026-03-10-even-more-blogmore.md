---
layout: post
title: Even more BlogMore
category: Coding
tags: AI, BlogMore, Coding, Copilot, LLM, Python
date: 2026-03-10 20:58:00 +0000
---

While the additions have, for sure, slowed down, I'm still tinkering away
with [BlogMore](https://blogmore.davep.dev/). Recent changes stem from the
fact that someone else has been mad enough to want to experiment with
rebuilding their blog with it too, which, if I'm honest, is massively
helpful with the ongoing GitHub Copilot experiment. Somehow it feels a
little different, ganging up with the agent to implement changes for someone
else's benefit.

Recent changes include:

- Tweaking the size and layout of the "social" icons that appear in the
  sidebar (this one was for my benefit)
- Making it possible to customise the title for the socials section in the
  sidebar (also for my benefit)
- Providing [control over the path used for
  posts](https://blogmore.davep.dev/configuration/#post_path) -- this one
  was a request that made a ton of sense, it's at this point it stops being
  a tool for me and starts being a more general tool

Next up is the first breaking change where I'm going to remove a feature.
This came from my very initial experiment last month, where I was
concentrating purely on building a tool for my blog and my blog alone. I'd
made it such that the `/attachments` directory in the content directory had
special status, and it would be copied over to the output directory in full.
Oddly, however, this never made it into the documentation.

Meanwhile, the `/extras` directory *also* had special status with its
content, full hierarchy included, being copied over but *moved up one level*
in the output. So, for example, `extras/humans.txt` became `/humans.txt` in
the resulting site, etc.

Presumably, at this point, you can see where this is going. Why the heck did
I have a special `attachments` folder being copied over, when a folder of
any name could live below `extras` and also get copied over?

So, now, my blog, which uses `/attachments` for all inline images and
covers, has been updated so that [the attachments live under
extras](https://github.com/davep/davep.github.com/tree/main/content/extras)
and it all works as it did before; no special messing with a special folder
name.

Given all this, the next release of BlogMore will remove treating
`/attachments` as a special case, making it less hard-coded for my habits
and more of a general tool that could be useful for others.

---

Mildly related to this: I did a lunchtime talk at work today, having turned
[Five days with Copilot](/2026/02/20/five-days-with-copilot.html) into a
20-25 minute presentation. It was fun to do. I've not written or given a
talk or presentation in a long time -- probably the last time was when I
helped run Newton's Astronomical Society in the early 2000s -- so the
preparation for this was a little daunting to start with.

While doing this, not wanting to break a long streak of never having used
PowerPoint, I discovered and gave [sli.dev](https://sli.dev) a go. Writing a
single Markdown file to power the talk was exactly my kind of approach. I
don't have any experience with any other such tools, but if you're ever
looking for something like this I recommend giving it a try.

I'm also open to suggestions of other options, given I might end up doing
this some more.

[//]: # (2026-03-10-even-more-blogmore.md ends here)
