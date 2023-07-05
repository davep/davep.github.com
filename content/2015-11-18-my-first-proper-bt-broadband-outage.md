---
layout: post
title: My first proper BT broadband outage
category: Tech
tags: Broadband, BT, Communication
published: True
date: 2015-11-18 11:25:29+0000
---

Until I moved about a year ago I'd always used Demon Internet as my ISP. I
stated with them during the old tenner-a-month days when there were only a
handful of points-of-presence to be called. I stuck with them through them
getting full local POP coverage, through having an ISDN line and then finally
ADSL.

When I moved though I decided it might be easier to just go with BT; for the
most part this hasn't actually been a bad decision. This week though I suffered
my first proper outage with them and it was rather frustrating.

It kicked off at around 2015-11-16 21:00. I noticed that Google Drive (in
Chrome) was complaining that it was offline. I then noticed that gmail and
a couple of other tabs in Chrome were complaining about the same thing. I
did a couple of local network checks and found nothing, checked the router and
it was connected and reporting just fine, so then I rebooted the router and
things appeared to improve.

For a short while anyway. Then I started to notice other problems; mostly that
some sites would time out, others not. Initially I was getting a lot of DNS
timeouts and, while I normally use Google's DNS servers (BT's have long had
lots of problems[^1]), I tried switching back to BT's own and that appeared
to improve matters. For a while anyway.

I mentioned the issues on twitter and got a handful of replies from different
people running into similar issues. It was clear that this wasn't just me. I
then went looking for BT's broadband status page but hilariously was unable
to load it because of the problem.

This is my first bit of real frustration with them. Here's how the page
looks inside a desktop browser:

![Status in desktop browser](/attachments/2015/11/18/Screen Shot 2015-11-18 at 10.42.40.png)

Now compare it as seen inside Android Chrome on my Nexus 6:

![Status on my phone](/attachments/2015/11/18/Screenshot_20151118-104156.png)

Apparently they have decided that I'd never want to be able to check why my
broadband might be down, from a mobile device. Yes, sure, there's the option
to put my phone number in -- perhaps it tells me after I've done that -- but
I don't even know my land line number; I don't use it as a phone most of the
time and so never bother remembering it. The main point here is why the hell
wouldn't they include the same useful information as the desktop view? Or
perhaps use geolocation of the phone to narrow things down if they feel the
need.

Anyway, I gave up and went to bed. In the morning things were no better but,
after another router reboot, I did manage to get a view of the status:

![Finally got to see broadband status](/attachments/2015/11/18/Screen Shot 2015-11-17 at 10.29.47.png)

Finally! Acknowledgement of the problem. Worryingly though it was dated almost
12 hours after I first noticed the problem. From what I can see that date and
time isn't the date and time the status was last updated, it's the date and
time it was first added. That suggest that they really hadn't noticed the
problem all night. It's not like it was a problem that was hard to notice,
at least from a customer's point of view. Check this graph from a [down
detector site](http://downdetector.co.uk/problems/bt-british-telecom):

![It really was down](/attachments/2015/11/18/Screen Shot 2015-11-17 at 10.27.07.png)

You'd think that a company as big as BT would have something in place that could
catch network problems, especially ones that are able to be caught with a simple
crowdsourcing "press this button if you have a problem" approach.

But... nope. Appears not. O_o

Anyway, a couple or so hours later the problem was finally fixed:

![Finally got to see broadband status](/attachments/2015/11/18/Screen Shot 2015-11-17 at 13.01.00.png)

(Notice how the date and time is the same as earlier; so 100% not an update time
but a first-added time) I mentioned this on twitter:

<center>
<blockquote class="twitter-tweet" lang="en"><p lang="en" dir="ltr">Looks like BT broadband problems are resolved. Everything working that I can see, and this... <a href="https://t.co/m5Mo7vm5Yu">pic.twitter.com/m5Mo7vm5Yu</a></p>&mdash; Dave Pearson (@davepdotorg) <a href="https://twitter.com/davepdotorg/status/666602185233440768">November 17, 2015</a></blockquote>
</center>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

and I even got a reply (which I'd not gone looking for, so that was nice):

<center>
<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="en" dir="ltr"><a href="https://twitter.com/davepdotorg">@davepdotorg</a> Yes Dave we have the problem fixed, if you still notice a few issues then reset the hub and try again. ^Chris</p>&mdash; BT (@BTCare) <a href="https://twitter.com/BTCare/status/666642010045050880">November 17, 2015</a></blockquote>
</center>

Curious as to why it'd take almost 12 hours from the problem appearing to it
being acknowledged on their status, I thought I'd ask:

<center>
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr"><a href="https://twitter.com/BTCare">@BTCare</a> All looking good. Any reason why it took 12 hours to acknowledge?</p>&mdash; Dave Pearson (@davepdotorg) <a href="https://twitter.com/davepdotorg/status/666642201783480320">November 17, 2015</a></blockquote>
</center>

which got this reply:

<center>
<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="en" dir="ltr"><a href="https://twitter.com/davepdotorg">@davepdotorg</a> Sorry it took so long, identifing the source of the problems would have taken some time. ^Shane</p>&mdash; BT (@BTCare) <a href="https://twitter.com/BTCare/status/666666833148268548">November 17, 2015</a></blockquote>
</center>

which doesn't really make a whole lot of sense. Sure, you to spend time
identifying the source of a problem to *fix* it, but you don't need to do that
to notice and acknowledge that there's a problem. I've asked again but
haven't received any sort of reply as of the time of writing (I'm not expecting
one really).

What I take from all of this is that BT are shockingly bad at keeping people
informed of problems with their service when there's a large outage. I find
that kind of annoying. I don't mind that there are problems, I do mind when
a company can't take the time to clearly and quickly state "yup, it's us, it's
not you, we're looking into it..."

[^1]: Don't even get me started on how the HH5 won't allow setting of DNS servers in the hub itself. That's stupid and frustrating beyond words.

[//]: # (2015-11-18-my-first-proper-bt-broadband-outage.md ends here)
