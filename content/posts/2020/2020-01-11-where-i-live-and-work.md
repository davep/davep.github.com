---
layout: post
title: Where I live and work
category: Coding
tags: Emacs, shell
date: 2020-01-11 14:17:00+0000
---

It's no surprise that I spend a lot of time in Emacs. Especially when I'm
developing software, either for work or for personal fun, most of my time is
time spent in Emacs. While I do obviously flit over to Chrome, and mostly do
my CLI stuff in [iTerm2](https://iterm2.com/) (I really like
[eshell](https://www.gnu.org/software/emacs/manual/html_mono/eshell.html)
but it just can't replace a good terminal for me), I spend a lot of time
looking at Emacs.

Here's what my Emacs looks like:

![Screenshot 2020-01-11 at 13.49.04.png](/attachments/2020/01/11/Screenshot 2020-01-11 at 13.49.04.png#centre)

Key elements for me are as follows:

# Light background

Something I've never really got on with when it comes to code editing is
dark themes and dark backgrounds. I find it too much of an eye strain.
Oddly, I tend to prefer dark themes everywhere else, but not when it comes
to working in Emacs. The theme I use is [the built-in adwaita
theme](https://github.com/davep/.emacs.d/blob/b9a3df42f0708eabc31a6176d69a67bbdf31a087/init.d/init-style.el#L12-L13).

# Less boring mode line

I make use of [powerline](https://github.com/milkypostman/powerline) to
[make the mode line a bit less
boring-looking](https://github.com/davep/.emacs.d/blob/b9a3df42f0708eabc31a6176d69a67bbdf31a087/init.d/packages/init-packages-melpa.el#L386-L399).
While the colour scheme is such that it's kept in line with the light look,
the style is nice in that it sort of matches the style of prompt I use in my
shell.

![Screenshot 2020-01-11 at 14.05.39.png](/attachments/2020/01/11/Screenshot 2020-01-11 at 14.05.39.png#centre)

# Full screen

I always run Emacs as a full-screen application, then splitting it into
different tiled windows using its own internal window handling. This is
something I've done from way back when I got started with my first GNU/Linux
desktop machine, and still like to do on macOS.

I also [run Emacs as a server](https://github.com/davep/longmacs.el) and
then use [a little wrapper around `emacsclient`](https://github.com/davep/e)
to open files (both locally and remotely) from the command line in that
Emacs session.

# Comfortable eshell when I need it

Although I say above that I generally don't use `eshell`, preferring to use
a full-featured terminal application, in combination with
[fish](https://fishshell.com/), I do sometimes dip into eshell for quick
things. So of course I have that configured to feel comfortable too.

![Screenshot 2020-01-11 at 14.10.07.png](/attachments/2020/01/11/Screenshot 2020-01-11 at 14.10.07.png#centre)

I do this easily [thanks to
`eshell-git-prompt`](https://github.com/davep/.emacs.d/blob/b9a3df42f0708eabc31a6176d69a67bbdf31a087/init.d/packages/init-packages-melpa.el#L181-L192).

[//]: # (2020-01-11-where-i-live-and-work.md ends here)
