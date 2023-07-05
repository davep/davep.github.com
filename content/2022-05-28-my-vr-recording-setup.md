---
layout: post
title: My VR recording setup
categories: []
tags: VR, YouTube, PCVR
date: 2022-05-28 17:01:00+0100
---

# Introduction

For well over a year now I've been recording my VR gameplay [and uploading
it to YouTube](https://www.youtube.com/user/daveporg). Less as a "content
creation" thing, more as a nice record of games I've played and, on
occasion, as a little bit of help to others; in the past I've watched other
folk play games I like to get ideas for approaches to them, and I've also
received the odd comment now and again where my play-through has helped
someone else.

A question I've had a couple of times is what I use to do the recording, so
I thought I'd make an effort to write it all down here.

First up, a couple of things to note: I started recording PCVR around April
2021 and the initial setup was a bit trial-and-error and Google searching
and blog reading. As such, not all of the details of *how* to set up will be
here, and I may even miss off some stuff I changed and is worthy of note; at
the same time I might mention stuff that's just an obvious default.

Consider this blog post as being a written version of one of my videos: it's
for my own fun and benefit and might also help me in the future should I
want to apply some of this again, and if it helps someone else that's a
lovely bonus.

# The Hardware

While it's not exactly the point of this post, I guess it's worth mentioning
the hardware I use as of the time of writing. Given this is about PCVR, I of
course have a PC which is running Windows. The machine information within
Windows says it's a:

> Intel(R) Core(TM) i5-10400F CPU @ 2.90GHz

Warning: I don't do hardware. I buy it from time to time, but hardware
leaves me bored. It runs VR on a PC. This is fine.

The machine itself has 16 GB of memory, is running Windows 10 Home and has a
GeForce RTX 3060 for handling the graphics.

The headset I'm using is a~~n Oculus~~ Meta Quest 2. I've had this
since around November 2020, playing Quest-native games for the first few
months, until I cracked and got the PC mentioned here to get into PCVR.

The headset is connected to the PC with [a USB
cable](https://www.amazon.co.uk/gp/product/B08MJDNV4F/).

Finally, for recording voice, I use a [USB lapel microphone with a really
long cable](https://www.amazon.co.uk/gp/product/B08T1S7NRP/?th=1).

It should be said that, yes, sometimes, I do get a little caught up in
things with two cables hanging off me. If I could give one tip here it would
be that running the microphone cable up your trousers and shirt makes life a
ton easier. As a bonus I have the USB cable for the headset running around
the headset's strap and connected to it at the back and then running down my
back.

# OBS Studio

The core software used is [OBS Studio](https://obsproject.com/). This has
got to be one of the best bits of free software I've ever used, in terms of
interface and what it delivers.

Years back my son used to record and upload gameplay to YouTube and I can
remember him having no end of issues using different recording software;
some working with one game but not another, some other working with a
different set of games, video and sync issues, etc... Lots of pain quite
often. With OBS Studio the only issues I've ever had have been my own
mistakes.

At this point I have to confess that when I set it up I didn't make a point
of keeping a recording of what I changed -- I was experimenting and not
expecting much to come of it. So what I note here are the things that feel
like they're important, and only the things that relate to recording PCVR,
not streaming it (that might end up being a different blog post).

That said, here are things I seem to remember as being key:

## Output Settings

The items in the output pane in settings that I have and which might be
important are:

- `Output Mode:` Simple
- `Recording Quality`: High Quality, Medium File Size
- `Recording format`: mkv
- `Encoder`: Hardware (NVENC)

I do remember the recording format being set to `mkv` as something that's
really important. I think it's `mp4` by default, or was when I first
installed, and if your machine crashes or OBS were to crash or something,
you could end up with footage that can't be used. Using `mkv` means you can
still use the footage (as I understand it). It does mean that once you're
finished you have to use the "remux" option under the `File` menu, but
that's a small price to pay.

I can say that at least once I've had to hard-reboot my machine when a game
and SteamVR and the like all got upset. I likely saved 45 minutes or more of
footage thanks to `mkv`.

# Video Settings

Nothing really special in here, I simply have both the base and output
resolutions set to the desktop resolution. This *might* be something for me
to tinker with in the future, but so far I've not run into any problems.

# VR Capture

Now, of course, all of the above is great and fine and all but there's the
issue of how you capture the VR gameplay. I approach this a couple of
different ways. The first is I use the [OpenVR Capture plugin for
OBS](https://github.com/baffler/OBS-OpenVR-Input-Plugin). This makes
capturing footage from SteamVR really easy. The only downside I found is
that out of the box there's no default crop setting for using a Quest 2 (or
I guess the Rift, as the Quest 2 sort of appears as a Rift to SteamVR
games). As such I remember playing trial and error with that until I was
happy I was getting as much footage as possible without having black bars
and the like.

Something I also like about the OpenVR Capture plugin is you can say if you
want to capture the left or right eye. Normally not that big a deal for some
things, but if you're playing a shooter and want people to see exactly what
your dominant eye is seeing, that matters.

Sadly, of course, not every game can be captured with that plugin. So far
I've found that any game that can't be has its own mirror window on the
desktop. In that case I use a `Game Capture` source and set it to capture
that specific window. I could of course just get it to capture the focused
window or something like that but I prefer to know that it's only grabbing
what I want it to grab.

# Conclusion

That's pretty much it I think. There's not a lot to it, although on occasion
a lot can go wrong. Mostly it's a wonder any of it works. I mean, think
about it, I have a computer with two screens strapped to my face, with two
controllers in my hands talking to it; it's then connected via the Oculus
Link to the Oculus Home; from which I start up SteamVR; and from the SteamVR
home I start up the game and then "live" inside the game. It's a virtual
world inside a virtual world inside a virtual world inside a real world;
with lots of software along the way, all talking at once.

That is then being recorded.

Sometimes, on occasion, it takes a reboot or five to make it all work
together.

Really, it's a wonder it ever works. ;-)

[//]: # (2022-05-28-my-vr-recording-setup.md ends here)
