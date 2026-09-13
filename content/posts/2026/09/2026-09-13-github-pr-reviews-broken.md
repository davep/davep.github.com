---
title: "GitHub PR reviews broken"
date: "2026-09-13 15:19:16+0100"
category: Tech
tags: [GitHub, web]
---

Late on last week I was doing a PR review at work and noticed that, for some
odd reason, the author of the PR seemed to have absolutely nuked all of the
indentation in the code. While not a problem given the nature of the files I
was reviewing, I wasn't happy with their apparent disregard for style and
good practice, and was about to leave a remark and a request for changes.
But something seemed off. So I did a refresh of the page and... everything
fell into place.

Weird.

Since then I've seen the issue on multiple machines. To be fair, each time
it's been in Safari, and each time I've been busy with something else so
haven't had the chance to really dive into it. But given it's suddenly
cropped up, at the same time, on multiple machines, with nothing else
changing, it feels like something on the GitHub side of things.

![Broken code review](/attachments/2026/09/13/borked-code-review.webp#centre)

Perhaps I'm letting a bit of bias creep in here, but I feel like this sort
of thing is happening more and more on GitHub. It's not that long back since
[social previews suddenly
broke](/2026/08/21/github-social-preview-is-broken.html), for example. It's
hard to shake the idea that changes are being made without regard to
comprehensive testing, and likely without regard to how things connect.

Now, at this point, it would be easy to reach for the *"well they're
obviously using agents to do most of the work"* argument -- and I'm sure
plenty of people would -- but that doesn't quite fit with my experience.
Having experimented with such tools for a good chunk of this year now, both
for personal and, more recently, professional projects, I've generally found
that such tooling easily helps with catching such issues.

Plenty of times now, when using something like
[Antigravity](/tag/antigravity/) or Claude Code to work on some code, I've
found that with reasonable care (you know: the sort of care you'd put into
your work anyway) you can quickly and easily uncover connections and
knock-on effects you might not have immediately noticed. Moreover, if LLMs
are useful for anything when it comes to coding, it's for writing tests[^1].
With that in mind you should be able to reasonably expect the number of
silly bugs to go down.

Unless, of course, there's no human in the loop anywhere, or the human in
the loop lacks adequate training and experience, or, I guess, they simply
lack the ability to give a shit.

I wonder when this particular issue will get fixed? I should probably go and
see if it's reported in the GitHub forums anywhere. I know for sure that
there's little point in actually reporting it as a bug; my experiences with
that in the past haven't been great, and the GitHub subreddit has seen
enough stories of people getting nowhere.

[^1]: Arguably they're a little too good at it to the point of coming round
    the other side and doing badly again, if you don't keep an eye on things.

[//]: # (2026-09-13-github-pr-reviews-broken.md ends here)
