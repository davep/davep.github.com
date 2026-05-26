---
title: Still confused about Antigravity quotas
date: 2026-05-26 10:01:05+0100
category: AI
tags: Coding, Gemini, Google, Antigravity
cover: /attachments/2026/05/26/agy-quota.webp
---

While it did appear something had changed for the better [yesterday
evening](/2026/05/25/something-changed-with-antigravity.html), things looked
different again this morning. Before getting to work, I did a couple of
quick changes to [BlogMore](https://blogmore.davep.dev/); this time
[Antigravity](/tag/antigravity/) seemed to use up a bit more quota in the
same amount of time as I was working last night, but this time the reset
window is much bigger.

![Antigravity quota](/attachments/2026/05/26/agy-quota.webp#centre)

I'm sure there's a method to this, but at the moment I'm really unclear what
it is.

I guess I could ask it...

Yeah, let's do that.

---

*Can you explain your quota cooldown time for me? Sometimes it seems to
count down from 1 hour, others 5. Am I not reading this correctly?*

You are reading the quota cooldown correctly! The reason the timer
fluctuates between 1 hour, 5 hours, or other times is due to how the rolling
usage window and compute-based limits work.

**1. Rolling 5-Hour Window**

Your usage limit is evaluated on a rolling window (typically 5 hours) rather
than resetting at a fixed time of day.

- If you see a 5-hour cooldown: You likely used a large portion of your
  compute capacity very recently. You have to wait for that recent window to
  clear.
- If you see a 1-hour cooldown: You are close to the edge of your rolling
  window. A batch of high-compute requests you made 4 hours ago is about to
  fall out of the 5-hour window, which will free up capacity for you in 1
  hour.

**2. Compute-Based Usage (Not Message Count)**

Your quota is consumed by compute rather than a flat number of messages.
Compute is affected by:

- Chat Length: Every time you send a new message, the model re-processes the
  entire chat history. Longer conversations consume your quota much faster.
- Task Complexity: Tasks like code generation, deep thinking, or agentic
  workflows require more processing power and consume more quota.

**Tips to Manage Your Quota:**

- Start New Chats: For new topics or tasks, start a fresh conversation. This
  prevents the model from having to re-read long histories and saves
  significant compute.
- Use Clear, Targeted Prompts: Try to combine instructions rather than
  sending multiple short follow-up messages.

---

So, I don't think I'm any wiser after that. The explanation for the 1-hour
countdown I saw last night has no connection to anything I did yesterday; I
wasn't using Antigravity 4 hours earlier when I checked the quota near the
end of that session. Guess I need to go and find and RTFM. Just like we used
to in the good old days.

[//]: # (2026-05-26-still-confused-about-antigravity-quotas.md ends here)
