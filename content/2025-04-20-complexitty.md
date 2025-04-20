---
layout: post
title: Complexitty
category: Coding
tags: Python, terminal, textual, mandelbrot
date: 2025-04-20 09:30:00 +0100
cover: attachments/2025/04/20/complexitty-social-banner.png
---

[![Complexitty](/attachments/2025/04/20/complexitty-social-banner.png)](https://complexitty.davep.dev/)

Much like [Norton Guide readers](https://www.davep.org/norton-guides/) or
the [5x5
puzzle](https://github.com/davep?tab=repositories&q=5x5&type=&language=&sort=),
code that has fun with the Mandelbrot set is another one of my goto
exercises. I've written versions in many languages, and messed with plot in
some different environments, as varied as [in VR on the
web](https://www.youtube.com/watch?v=18ytRZrHL34) to [wearable
items](https://www.redbubble.com/i/t-shirt/Self-Documenting-Mandelbrot-by-davepearson/1341910.0S66D).

Back in the early days of [my involvement with
Textualize](https://blog.davep.org/2024/03/28/goodbye-textualize.html) I
[wrote a deliberately worst-approach
version](https://github.com/davep/trMandelbrot) using that framework. The
whole thing was about taking a really silly approach while also
stress-testing Textual itself. It did the job.

Later on I did [a second version that targets
Textual](https://github.com/davep/textual-mandelbrot). This time it did a
better job and was the catalyst for building
[`textual-canvas`](https://textual-canvas.davep.dev/). This version was
intended more to be a widget that happened to come with an example
application, and while it was far more better than the on-purpose-terrible
version mentioned above, I still wasn't 100% happy with the way it worked.

Recently I did some maintenance work on `textual-canvas`, cleaning up the
repository and bringing it in line with how I like to maintain my Python
projects these days, and this prompted me to look back at
`textual-mandelbrot` and rework it too. Quickly I realised it wasn't really
sensible to rewrite it in a way that it would be backward compatible (not
that I think anyone has ever used the widget) and instead I decided to kick
off a fresh stand-alone application.

[Complexitty](https://complexitty.davep.dev/) is the result.

![Complexitty on startup](/attachments/2025/04/20/complexitty.png)

Right now the application has all the same features as the `mandelexp`
application that came with `textual-mandelbrot`, plus a couple more. Also
it's built on top of [the common core
library](https://github.com/davep/textual-enhanced) I've been putting
together for all my own terminal-based Python applications. As time goes on
[I'll add more
features](https://github.com/davep/complexitty/issues?q=is%3Aissue%20label%3ATODO%20label%3AEnhancement).

![Zoomed in with Complexitty](/attachments/2025/04/20/complexitty-red.png)

As with most of my recent TUI-based projects, the application is built with
comprehensive help for commands and key bindings.

![The help screen](/attachments/2025/04/20/complexitty-help.png)

and there's also a command palette that also helps you discover (and run)
commands and their keyboard bindings.

![The command palette](/attachments/2025/04/20/complexitty-commands.png)

Complexitty is licensed GPL-3.0 and available [via
GitHub](https://github.com/davep/complexitty) and also [via
PyPI](https://pypi.org/project/complexitty/). If you have an environment that has
`pipx` installed you should be able to get up and going with:

```sh
pipx install complexitty
```

It can also be installed with
`Homebrew` by tapping `davep/homebrew` and then installing `complexitty`:

```sh
brew tap davep/homebrew
brew install complexitty
```

[//]: # (2025-04-20-complexitty.md ends here)
