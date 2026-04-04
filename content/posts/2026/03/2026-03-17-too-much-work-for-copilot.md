---
layout: post
title: Too much work for Copilot?
category: AI
tags: Python, AI, LLM, Copilot, GitHub, BlogMore
date: 2026-03-17 14:27:00 +0000
cover: /attachments/2026/03/17/too-many-requests.png
---

I don't know if it's just that GitHub Copilot is having a bad time at the
moment, or if I've run into a genuine problem, but all isn't well today.
After merging [last night's
result](/2026/03/17/when-your-model-leaves-you.html) I kicked off [another
request](https://github.com/davep/blogmore/issues/306) related to [a group
of changes I want to make to
BlogMore](https://github.com/davep/blogmore/issues/298). It's a little
involved, and it did take it a wee while to work on, but mostly it got the
work done.

Again, as I said in the earlier post, I won't get into the detail of these
changes yet, but they're fairly extensive and do include some breaking
changes, so it's probably going to take a wee while to have it all come
together. Claude's first shot at the latest change was almost there but with
the glaring bug that it did all the work but didn't actually add the part
that *reads the configuration file settings and uses them* (yeah, that's a
good one, isn't it?).

So [I asked it to fix
it](https://github.com/davep/blogmore/pull/307#issuecomment-4074343536). It
went off, worked on the issue, and then suddenly...

![Denied](/attachments/2026/03/17/too-many-requests.png#centre)

This surprised me. After the past few weeks I've had sessions where I've
requested it do things way more frequently than this morning. I'm also
nowhere near out of premium requests either:

![Number of requests left](/attachments/2026/03/17/requests-left.png#centre)

While the error, as shown, might be valid and might be down to my actions,
it's massively unhelpful and doesn't really explain what I did to cause this
or even how I can remedy it. This is made all the more frustrating by the
fact that it seems to be saying I need to wait `<duration>` to try again.
Yes, literally a placeholder of `<duration>`. O_o

One thing is for sure: this is another useful experiment in the current
experiment. It's worth having the experience of having the tool screw with
the flow. It doesn't come as a surprise, but it's a good reminder that using
an agent that is hosted by someone else means you fully rely on their
ability to keep it working, the whims of their API limits, and perhaps even
your ability to pay.

[//]: # (2026-03-17-too-much-work-for-copilot.md ends here)
