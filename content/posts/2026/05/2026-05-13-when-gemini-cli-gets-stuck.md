---
title: When Gemini CLI gets stuck
date: 2026-05-13 20:27:54+0100
category: AI
tags: AI, Coding, Gemini, Google
cover: /attachments/2026/05/13/thinking.webp
---

Another evening, and [another period of Gemini CLI getting stuck
thinking](/2026/05/12/the-other-unreliable-buddy.html). So this time I
thought I'd try something: cancel it while it was thinking and change the
model.

![Gemini Thinking...](/attachments/2026/05/13/thinking.webp#centre)

I was working [on something new for
BlogMore](https://github.com/davep/blogmore/pull/483) and, sure enough,
after a wee while, we got stuck in *"Thinking..."* mode. So I hit
<kbd>Escape</kbd> and asked to pick a different model. I chose to pick
manually, and went with `gemini-3.1-pro-preview`.

![Picking the model](/attachments/2026/05/13/pick-the-model.webp#centre)

I then literally asked that it carry on where it left off...

![Carry on](/attachments/2026/05/13/select-model.webp#centre)

...and it did! It worked. No more sitting around thinking for ages.

Watching the quota after doing this, it looks like the model I was using ate
quota faster, but that was worth it given I've never come close to hitting
full quota with Gemini CLI.

Once the immediate job was done, I went back to auto and it worked for a
bit, only to get stuck thinking again. I repeated this process and it did
the trick a second time. From now on I'm going to use this approach.

It does, again, highlight how unreliable these tools are, but at least I've
found a workaround that works for now.

[//]: # (2026-05-13-when-gemini-cli-gets-stuck.md ends here)
