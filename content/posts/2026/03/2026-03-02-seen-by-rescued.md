---
title: Seen by davep rescued
category: Creative
tags: blogging, photography, BlogMore, Twitter, Posterous, photoblog
date: 2026-03-02 17:18:00+0000
cover: attachments/2026/03/02/final-message.jpeg
---

![Final Message](/attachments/2026/03/02/final-message.jpeg#centre)

Since mid-2023 [my photoblog has been
broken](/2023/08/20/seen-by-davep-broke-again.html). As I mentioned at the
time, the issue was that this second incarnation of the blog had started
life as a proper
[mashup](https://en.wikipedia.org/wiki/Mashup_(web_application_hybrid)) of
some web tools, and the heart of it was Twitter.

It all started to fall apart when Twitter got its new owner, and APIs became
expensive, and other tools would not or could not work with it any more, and
then it really fell apart when I finally nuked my account.

So since then the blog has been sat about, unused and unloved, with a lot of
broken links and images.

Thankfully, though, the pipeline that I had going had been designed with
this sort of problem in mind: part of what I had going also made a backup of
the photos I took to Google Drive and to Google Photos. So when I got to a
point the other day where [BlogMore](https://blogmore.davep.dev/) was usable
I decided I should rescue the photos and rebuild the blog.

After downloading the full feed of the Blogger.com-hosted blog, I threw
together some Python code that took the data (thanks to
[`feedparser`](https://github.com/kurtmckee/feedparser) for helping with
that), matched up the posts with the images I had in Google Drive, slugged
the names, wrote some Markdown and copied some images, and [I had the source
of a fresh blog](https://github.com/davep/seen-by).

The result of all of this can be seen up on
[seen-by.davep.dev](https://seen-by.davep.dev/).

I strongly suspect this is going to remain a pretty static site. At the
moment I've given no thought whatsoever as to how I might have this populate
in the way the old version of it did. Quite simply the old version was:

1. Take photo
2. Post to Twitter with a specific hashtag
3. Have IFTTT notice this and create the blog post, make backups
4. ...
5. Profit?

I suppose, this time around, I could have something monitor [my Mastodon
account](https://fosstodon.org/@davep), or my [pixelfed
account](https://pixelfed.social/davepearson), and then trigger a similar
process; but then that would need something akin to IFTTT running and
interacting with GitHub and creating the Markdown and kicking off a build
process and...

Eh, maybe one day. For now, though, I'll be happy that I've rescued this
particular incarnation of my photoblog and then think about if and how I
carry on with something similar in the future.

Meanwhile... this has got me thinking. The *original* blog is [backed up on
WordPress](https://seenbydavep.wordpress.com/). It's been sat there, all sad
and neglected, ever since Posterous disappeared. I wonder if I can export
all the data from there and mash it into this new version...

[//]: # (2026-03-02-seen-by-rescued.md ends here)
