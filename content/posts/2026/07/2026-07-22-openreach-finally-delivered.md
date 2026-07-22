---
title: "Openreach finally delivered"
date: "2026-07-22 16:10:35+0100"
category: Life
tags: [BT, Broadband, Business, EE, Mac, Openreach, macOS, networking]
series: ["Trying to get full fibre from EE"]
---

The day after [the last failed attempt to install
fibre](/2026/07/13/let-down-by-openreach-again.html), I got a follow-up
message from [Openreach](/tag/openreach/), pretty much not telling me
anything I didn't already know:

> We came to see if we can connect your property to our Full Fibre network yesterday.
>
> The good news is we can, but the engineer found that the existing network
> connection point wasn't suitable for private land's underground
> connection, so we need to plan a new way to bring the fibre cable to your
> home, which may also require a specialist engineer for a flat roof
> connection.
>
> We're really sorry for the delay, but we're on it and will update you
> again in the next 10 days (we're usually much quicker).
>
> We promise Full Fibre's worth the wait. It's the UK's most reliable
> broadband technology.

The flat roof thing was... interesting, but okay, I'm sure they know what
they're doing and that it's some automated system with a restricted set of
outcomes.

Skip forward one day and I get an SMS out of the blue:

> Hi, it's Openreach on behalf of EE/BT.
>
> Sorry we missed you.
>
> Book a new date for your Full Fibre installation here: *[removed]*

The *"Sorry we missed you"* was very odd. They didn't miss me. I saw them
two days earlier. But, again, okay... I followed the link and it also seemed
to be written as if one of us had missed an appointment and I needed to pick
another day. Anyway, I ignored what it said and just used the date picker to
pick the next available day (which was today: as in the day I'm writing
this).

Fast forward to today and there's a knock on the door at around 08:30.
Around two hours later, and this is what I was seeing:

![My new speeds](/attachments/2026/07/22/new-speeds.webp#centre)

To be clear: this isn't the actual speed of the connection. This was a quick
test from my Mac, in my office, via the Wi-Fi connection. I don't currently
have a Mac or PC wired into the router so can't measure the full speed.
Testing on the router itself, it's much closer to 943Mbps/100Mbps. But,
yeah, I'm good. I finally have full fibre again!

There was an immediate downside though. Once it was all set up, with the new
router (which I swapped to as it has Wi-Fi 6, so why not?), I noticed that
the ping times between my Macs were all over the place; this was also
noticeable in that the `ssh` connections were so jittery to the point of
being almost unusable.

Bugger.

So I did a bunch of digging online and, without getting too deeply into it
(because I'm not a networking guy): the problem is AirDrop/Sidecar. They
don't play well with a Wi-Fi 6 connection, so do stuff in the background
that causes your ping times to be all over the place.

The solution? Turn this off for the Wi-Fi connection on the affected Macs:

![Wi-Fi 6E off](/attachments/2026/07/22/wifi-6-off.webp#centre)

I can't find anything that suggests I'm going to regret doing this for the
couple of Macs in my office, and for my [MacBook
Air](/2026/03/28/hello-macbook-air-again.html), and having done it, the
performance is fine again.

This is why I avoid anything to do with networking: it always seems like if
you improve one thing, it degrades some other thing, and it's only ever
fixed by remembering to tweak some reasonably obscure setting somewhere on
some particular item of hardware.

Still... I HAVE FULL FIBRE AGAIN!

Finally, I can think about [doing the odd stream
again](/2026/05/15/planning-on-returning-to-streaming.html).

[//]: # (2026-07-22-openreach-finally-delivered.md ends here)
