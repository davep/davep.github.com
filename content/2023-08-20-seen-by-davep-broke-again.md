---
layout: post
title: Seen by davep broke (again)
category: Creative
tags: blogging, photography
date: 2023-08-20 09:25:00+0000
---

Almost [seven years ago](/2016/11/15/seen_by_davep_(the_return).html) I took
up maintaining an ad-hoc photoblog again. I say again because I'd had one
once before. I'd kicked that off back in the late 200xs, with my little HTC
Magic, and hosted it on
[Posterous](https://en.wikipedia.org/wiki/Posterous). Eventually Posterous
was shut down, mostly because the company (or at least the team behind it))
had been [bought up by
Twitter](https://web.archive.org/web/20130424063619/http://blog.posterous.com/big-news).
When kicking off the blog this time I decided on a few things:

- I'd host it on Blogger.com; it had been around for long enough, and of
  course [Google could be trusted to keep something that big up and running
  for good](https://killedbygoogle.com/).
- I'd keep multiple backup copies of the images and file them in useful ways
  (I keep copies in Google Photos, on Google Drive, on iCloud and locally).
- As much as possible I'd automate the process of doing some, if not all of
  this.

At this point, while it was kind of old as an idea, this felt very much like
one of those things that was perfect to do in a [Web
2.0](https://en.wikipedia.org/wiki/Web_2.0) way; the good old reliable
[mashable
web](https://en.wikipedia.org/wiki/Mashup_(web_application_hybrid))!

So the plan became this:

- Every post would be a tweet, posted to Twitter with a `#photoblog` tag.
- I'd use [ifttt](https://ifttt.com/) to keep an eye on my tweets and when
  it saw one with that tag it would extract the image, make a post to
  Blogger, drop a copy into Google Drive, and do a couple of other things
  too.
- Every week or so I'd do some manual checks to make sure everything is
  looking okay.

This worked. Mostly. It ran fine for a few years, with very few problems.
I'd take a photo, manipulate the heck out of it for the emotional effect I
was going for (that was the point of the blog; it was all about the messing
with the image), tweet it, and Web 2.0 magic would happen.

Then the odd issue started to crop up. At one point Twitter made changes to
how images were stored, or something, and the ifttt recipe broke for a wee
while; then they changed the way that public posts could be seen (long
before the Musk-era bullshit) and that broke things again, and so on. I
forget the details but at every point I was able to nurse it back to life
and things carried on.

Recently, of course, it all fell apart when Musk took over Twitter and
massively ruined it, turning it into the steaming pile it is now[^1]. I've
honestly lost track of which change broke what, and of course I also gave up
even trying to use Twitter (the drip, drip, drip of right-wing hate politics
got to a point where I could not find a way to make it work any more). So
that's when I decided to cut Twitter out altogether.

This had actually started a little earlier than that, when the whole API
fiasco kicked off. When that came in ifttt had to remove Twitter things from
its free tier; I was on the free tier. I was on the free tier only because I
didn't need anything the paid service offered. If Twitter had been "normal"
and this change had been made I'd have happily paid -- I don't mind paying
for things I find useful.

But, nope, given all the context, I bailed.

So by that point I decided the easiest thing to do was to simply hand-add
posts to Blogger, and also along the way post to [a pixelfed account
instead](https://pixelfed.social/i/web/profile/496199122963740964),
reposting those posts from [my Fosstodon
account](https://fosstodon.org/@davep). Not ideal, needing more manual
input, but also I was thinking that once I find a good flow I could probably
automate the whole thing again.

Anyway, that's the point I'd reached. Twitter was 100% out of the workflow,
there was a bit more manual intervention, but the [primary location for the
photos](https://seenbydavep.blogspot.com/) was still getting updated.

Then yesterday I noticed this:

![Broken images in my photoblog](/attachments/2023/08/20/borked-photos.png)

I don't actually quite know exactly what's going on here, and at this point
I really don't care. My working hypothesis is this: when ifttt added the
images to the Blogger posts, it was doing so in a way that it was using the
image hosted by Twitter. Because of this, either due to some change in the
Twitter API, or perhaps because I've locked down my Twitter account, the
images can't be served any more. That's my best guess anyway.

I don't really care to dig deeper than that.

But, yeah, this is another example of the long-growing rot of the dream of
Web 2.0. I'm not surprised; I'm not angry; I'm just disappointed.

Thankfully I have all the images saved (see backup options above), so I can
go back and edit the posts and drop fresh copies of the images into them.
There's 100s of posts affected so this is going to take quite a while; I
mean, sure, I could probably do it in a day if I sat and did nothing else,
but I have other things to do.

Another option would of course be to create a fresh blog using my own tools;
that would be simple enough. I have the images, they're all set with the
right date and time, recreating things would be fairly trivial (post titles
a slight problem but I could work around that); a tool like mkdocs or
Pelican plus some Python code to recreate the posts from the images would be
a fun couple of hours mucking about. But... I have a lot of posts on Blogger
and all the URLs are stable and still there many years later.

Perhaps I could automate the "fixing" of the broken posts? I wonder what the
Blogger API is like to work with?

*PS: If you've read this and feel that what's *really* needed is a "helpful"
comment that self-hosting is the solution; please sit on that and read the
above again (and, you know, look over the rest of this blog and the entirety
of my time and content on the Internet in general and the Web in particular,
going back to the mid-90s).*

[^1]: Seriously, if you are reading this and you're still maintaining a
    Twitter account that you actively use, what the hell is wrong with you?
    Multiply that lots if you have a blue tick.

[//]: # (2023-08-20-seen-by-davep-broke-again.md ends here)
