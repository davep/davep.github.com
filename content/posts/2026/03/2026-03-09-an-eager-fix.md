---
title: An eager fix
category: AI
tags: AI, Coding, Copilot, GitHub, LLM, coding
date: 2026-03-09 12:56:00 +0000
cover: /attachments/2026/03/09/cover-eager.png
---

![An eager fix](/attachments/2026/03/09/changes.png#centre)

Yesterday, [while looking at starting to post to my photoblog
again](/2026/03/09/seen-by-me-revived.html), I noticed I'd missed a trick
when I added the [first](/2026/03/03/original-seen-by-davep-rescued.html)
and [second](/2026/03/02/seen-by-rescued.html) sets of photos when I
created [seen-by.davep.dev](https://seen-by.davep.dev): I'd left off any
`cover` frontmatter from all of the posts!

While I doubt it's super important -- I can't imagine people will be sharing
photos from the blog after all, especially not older ones -- it felt like
I'd failed to use [a useful
feature](https://blogmore.davep.dev/writing_a_post/#cover) that I'd made
sure [BlogMore](https://blogmore.davep.dev) had.

This was obviously easy to fix. I could just write a tool that would go
through all of the Markdown files, find the image that is being displayed in
the post, pull out the path to the file, and add a `cover` to the
frontmatter. Not exactly the hardest thing to write, but kind of boring for
a one-off fix.

So this felt like another good time to get Copilot to do the hard work.
Liking this plan, I [wrote an issue for the
prompt](https://github.com/davep/seen-by/issues/7) and set it to work.

The result was unexpected, and in retrospect this is how I should have
approached it in the first place; Copilot wrote the script, then ran it, and
then submitted the PR *including the script and all of the changes after
running it!* It's like it was super eager to do the fix so went ahead and
just did it.

![The resulting PR](/attachments/2026/03/09/cover-eager.png#centre)

This, for me, highlights a trick/approach I'm still not fully mindful of:
where I might once have written some throwaway code to do a job, run the
code, and then made use of the result, when it comes to using an agent I
always have the option of saying *what* I want done to the content of the
repository and just let it do it.

When I'm next faced with a problem like this, I think this is the approach
I'll take: rather than ask it to write the tool to do the work, I'll just
say what the work is I want done and let it go about it. *This* feels like
where an agent should shine and where it's really useful.

Meanwhile I can get on with the fun stuff.

[//]: # (2026-03-09-an-eager-fix.md ends here)
