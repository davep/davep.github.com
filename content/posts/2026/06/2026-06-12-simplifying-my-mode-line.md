---
title: "Simplifying my mode line"
date: "2026-06-12 19:06:26+0100"
cover: "/attachments/2026/06/12/mood-line-emacs.webp"
category: Emacs
tags: [Emacs, "Emacs Lisp", Lisp]
series: ["~/.emacs.d"]
---

Every so often I get the urge to change how Emacs looks. Ever since I
finally [fell to the dark
side](/2020/06/14/my-journey-to-the-dark-side-is-complete.html), my Emacs
has stayed looking pretty much the same. I like how it looks, but I do keep
having this urge to find a darker theme, and to also make things just a wee
bit more minimal.

At one point I was very much about, and in favour of, having as much
information as possible in [the mode
line](https://www.gnu.org/software/emacs/manual/html_node/emacs/Mode-Line.html).
Eventually I realised I didn't use that much and tried to declutter
somewhat, mostly cleaning up minor mode information with
[diminish](https://www.gnu.org/software/emacs/manual/html_node/use-package/Diminish.html).
Even then though, I had this feeling that there was still more information
in the mode line than I really needed.

So, just now, as an experiment, I've decided to start fairly clean. I've
dropped [powerline](https://github.com/milkypostman/powerline) and instead
decided to have a play with
[mood-line](https://github.com/emacsmirror/mood-line). Rather than use one
of its pre-configured formats, I've had a go at rolling my own:

```elisp
(setq mood-line-format
      (mood-line-defformat
       :left
       (((mood-line-segment-buffer-status) . " ")
        ((mood-line-segment-buffer-name) . " : ")
        (mood-line-segment-major-mode))
       :right
       (((mood-line-segment-vc) . "  ")
        (mood-line-segment-cursor-position))))
```

So far I'm really pleased with the result.

![My GNU Emacs](/attachments/2026/06/12/mood-line-emacs.webp#centre)

For any given buffer the mode line display is now:

- The status of the buffer
- The name of the buffer
- The major mode of the buffer
- The git status for what I'm working on
- The cursor position

Honestly, I'm struggling to think of anything else I really need to see.
Sure, I can imagine there's the odd minor mode I might need to know about,
but generally I either have them enabled all the time anyway, or it's
something so obvious that I know when it's not enabled.

I'm going to run with this for a while now and see how I feel. I can sense
that I might want to tweak a couple of things (at the moment the left-hand
side will move when I change the unsaved status of the buffer; on the right
there's nothing that tells me that this file I'm editing right now is new to
the repo and not part of it yet), but this basic configuration feels clean
and right.

Meanwhile... the search for [a theme](https://emacsthemes.com/) that is
darker and I actually prefer over [the sanityinc-tomorrow
themes](https://github.com/purcell/color-theme-sanityinc-tomorrow)
continues. I fear this is going to be a lot harder.

[//]: # (2026-06-12-simplifying-my-mode-line.md ends here)
