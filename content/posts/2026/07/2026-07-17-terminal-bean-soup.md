---
title: "Terminal bean soup"
date: "2026-07-17 20:54:32+0100"
category: Tech
tags: [Coding, FOSS, "Free Software", terminal, textual]
---

I'm sure most people reading this will be familiar with the concept of "bean
soup theory". In case anyone isn't, [here's how Wikipedia describes
it](https://en.wikipedia.org/wiki/Glossary_of_2020s_slang#B):

> A specific phenomenon described as a 'What about me' effect. An individual
> watches a video that doesn't pertain to them, but finds a way to make it
> about them anyway. Stems from a 2023 TikTok recipe for bean soup, with
> commenters saying "What if I don't like beans?"

I feel there's a very specific set of folk who love to "bean soup" anything
relating to terminals, and it's common to have them turn up in your mentions
if you happen to do *anything* in the terminal, or for the terminal, that
isn't about their purist opinions and how everything *must* be a Vim clone,
or worse.

I first encountered this when [I started working at
Textualize](/2022/10/05/on-to-something-new-redux.html). Unsurprisingly,
given the point, purpose and focus of [Textual](/tag/textual/), some folk
would turn up in the Discord server, in the issues, in the discussions, in
the mentions of posts in various places, and post their *very important
opinions* about how TUI software *must* work. Not... discuss their
preferences, or offer suggestions (there were plenty of people who were
pleasant like that, they were lovely to converse with), no: their engagement
was written as if every word that was mashed into their keyboard was a
well-crafted, handed-from-on-high RFC-like holy document that **MUST** and
**SHOULD** be followed[^1].

If I was being very charitable I could cut them some slack. If you're
building a framework for building applications for the terminal, there's a
good reason to make it at least possible for the application authors to
follow recognised best practice and to stick with hard-won conventions.
Indeed, Textual has some design choices that I think are deeply questionable
and misguided and I objected to them on more than one occasion. So, yeah, if
I was being charitable, I could cut them some slack.

I could... if they weren't such arseholes about it.

This gets worse though if you're building an application for the terminal,
especially if it's built as Free Software and the motivation is *to build
something for yourself and be kind enough to share*. It irks the hell out of
me when I build some application for myself, as a TUI, and then someone
turns up and starts complaining about *my* choice of default key bindings,
that work in *my* choice of terminal emulator and *my* configuration for
that emulator.

It's even worse when they do it in a way where they have to show their *very
deep knowledge* of terminals, and how they're very proud of just how lacking
in features and progress their own choice of terminal emulator is.

Dude...[^2] I know. I've used physical terminals. I've written COBOL on a
minicomputer using a line editor on some honking great dumb all-green
all-in-one box. I've even written code on a terminal using fan-fold paper.
I've used all sorts of terminal emulators. I spent well over a decade doing
shit inside `rxvt` which was running on my GNU/Linux server while displaying
on my Windows desktop machine.

I've [installed and tested plenty of terminal
emulators](https://github.com/Textualize/textual-key-recorder).

I'm well aware of the conventions and expectations. If
<kbd>Ctrl</kbd>+<kbd>C</kbd> doesn't quit... that is **my choice**. It's not
ignorance, it's not a lack of history with this stuff, it's a choice. For my
software.

So when you turn up and feel the need to tell me that some function keys
might not work in some terminal on some GNU/Linux box... I get it, you don't
like beans. If that's the case, how about you either don't make my hobby all
about *your* tastes and how I should build my application to suit you, or
how about you RTFM and configure my application so it works in your choice
of terminal?

I mean... we know you won't. We know you don't even care about the
application I'm having tons of fun building, that I'm spending time in a
joyous flow-state creating and tinkering with. You just care about making
the post all about you and your purity. We know you just care about showing
how smart you are.

We know you just can't resist the urge to reply-guy[^3].

We get it: you don't like bean soup. Nobody cares. Nobody asked.

[^1]: That reminds me: one day I should write a rant about the folk who obsess about the *"Zen of Python"*.

[^2]: Let's be honest: it's *always* a dude.

[^3]: Let's be honest: it's *always* a guy.

[//]: # (2026-07-17-terminal-bean-soup.md ends here)
