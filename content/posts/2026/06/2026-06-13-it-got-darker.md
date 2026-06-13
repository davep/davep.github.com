---
title: "It got darker"
date: "2026-06-13 10:49:48+0100"
category: Emacs
tags: [AI, Antigravity, Emacs, "Emacs Lisp", Lisp]
series: ["~/.emacs.d"]
cover: "/attachments/2026/06/13/darker-emacs.webp"
---

By pure coincidence, it's [six years ago
tomorrow](/2020/06/14/my-journey-to-the-dark-side-is-complete.html) that I
finally, after years of running [Emacs](/category/emacs/) with a bright
white background, moved to using a dark theme. It took a little bit of
getting used to but eventually I got very comfortable with it, and since
then have run everything I can in a dark mode too.

On occasion, in the last year or so, I've had this urge to move to something
darker. Also, in part, it's an urge to change things up a little. I felt it
was time for a refresh of how my Emacs looks. I've tried a few themes, but
none have ever stuck. When trying them I've run into various issues:

- It just didn't look nice at all
- Too many other things I use in Emacs didn't get themed
- It looked like there was going to be too much work to do to really theme
  things well
- It caused Emacs to crash[^1]

However, yesterday evening, after [making an effort to simplify my mode
line](/2026/06/12/simplifying-my-mode-line.html), I was determined to find a
darker theme that I would be happy with. I think I finally managed!

![An even darker Emacs](/attachments/2026/06/13/darker-emacs.webp#centre)

I've settled on `modus-vivendi` from [modus
themes](https://protesilaos.com/emacs/modus-themes). Out of the box it felt
right, and from what I can see in the documentation there's an amazing
amount of customisation you can do. The key point there too is the
documentation; there's so much of it, it's incredibly comprehensive.

For example: the default choice for the mode line is to have an unsubtle
border around it -- presumably to create a good contrast. I found that far
too distracting and was wondering what I could do about it. I didn't have to
wonder long, [the documentation addresses exactly that
situation](https://protesilaos.com/emacs/modus-themes#h:80ddba52-e188-411f-8cc0-480ebd75befe).

Another downside I ran into is that the colours that were showing in the
mode line, when I switched to `mood-line` yesterday, were gone. I spent a
short amount of time last night, and a good hour or so this morning, trying
to wrangle `mood-line` into something I liked, but I just couldn't get
anything sensible going. Eventually I cracked, fired up
[Antigravity](/tag/antigravity/), prompted it with:

> I am using mood-line for my mode line -- see
> `init.d/packages.d/melpa/mood-line.el` and
> https://github.com/emacsmirror/mood-line
>
> I am using https://protesilaos.com/emacs/modus-themes as my theme
>
> I would like to have finer control over the parts of the mode line I've
> configured. For example, I'd like the buffer name to stand out in an
> informative colour, but one that is part of the modus theme's colour
> scheme.
>
> Don't make changes yet, but help me understand how I should do this in a
> maintainable way.

and then spent about 20 minutes going back and forth, refining what I
wanted; this [got me a
result](https://github.com/davep/.emacs.d/blob/b9db88bae8f69f7e04f648642a88fe6f5ee02db2/init.d/packages.d/melpa/mood-line.el)
I'm happy with from a visual point of view. I still need to fully review the
code and the approach it took, but it isn't *too* far removed from what I'd
been trying myself.

Overall I'm pleased with the result, and this is the longest I've stuck with
a new theme (at this point I'm probably about 4 or 5 hours into working in
it). I think that says something significant. I can see myself still wanting
to tweak some aspects of it though. For example, the left-hand fringe
doesn't feel quite right, in a way I can't quite put my finger on. While I
want it to stand out from the main editing area, it feels... disconnected in
some way. Also the background colour of the mode line still feels like it
doesn't quite blend how I'd like.

Now to see if this lasts...

[^1]: Seriously, just the once, but that happened. I took that as a sign
    from the Lisp gods that I was doing something sinful.

[//]: # (2026-06-13-it-got-darker.md ends here)
