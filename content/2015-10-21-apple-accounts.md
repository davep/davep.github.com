---
layout: post
title: Apple Accounts
category: Tech
tags: Apple, OS X, iMac, SMB
published: True
date: 2015-10-21 15:36:19+0100
---

As much as I like my iMac, and as much as I am generally impressed with OS X
the more I use it, I'm constantly frustrated by the little issues I run into
that make life so much more interesting and which fly in the face of the
"it just works with Apple" fandom thing. The more I use the iMac, the more I
appreciate that Macs and OS X are just as "fun" as anything running Windows.

A little earlier was a good example. I wanted to share part of the iMac's
filesystem using [SMB](https://en.wikipedia.org/wiki/Server_Message_Block).
This seemed easy enough, the instructions on how to do it were clear and,
after following them, it utterly failed.

Brilliant.

So I Googled the issue a bit and ran into
[this handy forum post](https://discussions.apple.com/thread/6629743?start=0&tstart=0).
Apparently you can't actually connect with SMB if the account you're going to
be using to connect with is using iCloud login rather than a separate login.

Brilliant.

Not an obvious thing. Nothing said this was the case. According to the forum
post even Apple couldn't help the person who'd been trying to make it work.
But at least there was a workaround. All I'd need to do is split the password,
have a login for the machine that *wasn't* the iCloud login and I'd be all good.

I did it, it worked. I could browse the iMac's filesystem from my Windows
machine and all was good (I'd been able to do this the other way around
for ages and with no problems whatsoever).

![Finally got to allow SMB for me](/attachments/2015/10/21/Screen Shot 2015-10-21 at 15.29.11.png#centre)

Then I got curious.

What would happen if, once I had this set up, I "unsplit" the password and
went back to using the iCloud password to log in? That's when it got really fun.

To do this it asks you for the current password and also your iCloud password.
I entered both and...

![Finally got to allow SMB for me](/attachments/2015/10/21/Screen Shot 2015-10-21 at 15.28.46.png#centre)

Yup. It refuses, every single time, to accept that the iCloud password I'm
entering is valid. Trust me, it is. I'm entering the correct password. I can
log in to the iCloud website with it just fine. But when I use it to try and
"unsplit" my password.... nope.

Brilliant.

I've even tried disabling SMB sharing for my account, and even turning off
SMB sharing altogether. This doesn't seem to make any difference. Right now,
as far as I can see, now that I've split the password I can't go back
despite the fact that there's a method of doing it made available.

Brilliant.

[//]: # (2015-10-21-apple-accounts.md ends here)
