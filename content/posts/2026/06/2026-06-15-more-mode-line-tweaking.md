---
title: "More mode line tweaking"
date: "2026-06-15 19:47:15+0100"
category: Emacs
tags: [Emacs, "Emacs Lisp", Lisp]
series: ["~/.emacs.d"]
cover: "/attachments/2026/06/15/mode-line-update.webp"
---

The [simplification of my mode
line](/2026/06/12/simplifying-my-mode-line.html) is sticking, in that I like
how it's turned out and I find it more useful to have it this simple. But I
did notice something was missing: I'm a pretty constant but pretty casual
user of [projectile](https://github.com/bbatsov/projectile). I know it's a
package that offers a wealth of tools, yet mostly I just use it as a project
bookmark system. For this, though, it works well.

Given this, having a quick and easy way to check that I'm in the project I
think I'm in is a good idea. While I also have
[neotree](https://github.com/jaypei/emacs-neotree) open all the time, which
gives a fairly obvious clue, my eyes keep flitting down to the mode line.

The change I made the other day, deliberately, left the project off. I think
this was a simplification too far. So now it's back.

![Slightly updated mode line](/attachments/2026/06/15/mode-line-update.webp#centre)

The core of [my mode line
configuration](https://github.com/davep/.emacs.d/blob/944e88b18df1147597e0f7be117887bf51c37a77/init.d/packages.d/melpa/mood-line.el)
now looks like this:

```elisp
(setq mood-line-format
      (mood-line-defformat
       :left
       ((or
         (mood-line-segment-buffer-status)
         (propertize
          (mood-line--get-glyph :buffer-modified)
          'face 'my/mood-line-good-status))
        " "
        (mood-line-segment-buffer-name)
        (my/mood-line-segment-project)
        " "
        (mood-line-segment-major-mode))
       :right
       ((my/mood-line-segment-vc)
        " "
        (propertize
         (mood-line-segment-cursor-position)
         'face 'my/mood-line-cursor-position))))
```

A little busier than it started out, but still pretty clean. I do keep
wondering about the cursor position. In most buffers I have line numbers
showing to the left anyway, and it's rare (but not unknown) that I need to
know what column I'm in. I'm very tempted to remove the cursor position
altogether, then the right-hand side would just be the `vc` information, at
which point it might make sense to also move the project name over to the
right, given that the project and the repository information generally go
hand-in-hand.

I'll stick with this for now, but I can see this happening soon.

[//]: # (2026-06-15-more-mode-line-tweaking.md ends here)
