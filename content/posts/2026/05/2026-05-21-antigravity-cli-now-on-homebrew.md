---
title: Antigravity CLI now on Homebrew
date: 2026-05-21 08:58:41+0100
category: AI
tags: Antigravity, Coding, Google, Homebrew
---

Part of my morning routine, when I sit down at my desk, is to run updates.
This ritual updates, [amongst other
things](https://github.com/davep/fish/blob/main/conf.d/abbr.d/updates.fish),
anything I've installed via Homebrew. As this ran I noticed
`antigravity-cli` turn up as an addition to the index of things to install.

Noticing this, I decided to swap from the *"trust me, bro"* installation of
the CLI app from [yesterday](/2026/05/20/the-gemini-bait-and-switch.html) to
managing this via Homebrew. From what I could tell, cleaning yesterday's
installation was just a case of removing the 130MB `agy` executable that had
been dropped in `~/.local/bin`.

With that done, I did:

```sh
brew install antigravity-cli
```

and got a failure:

```
Error: It seems there is already a Binary at '/opt/homebrew/bin/agy'.
```

When installing `antigravity` via Homebrew yesterday, I seem to remember
seeing that it created an `agy` command as a wrapper for the GUI app at some
point. Assuming this will have been sorted out, I did a quick:

```sh
brew reinstall antigravity
```

followed by:

```sh
brew install antigravity-cli
```

and that all worked.

So, as of right now, I have a working Antigravity GUI application *and* an
Antigravity CLI and both of them are installed via Homebrew.

Feels tidy.

[//]: # (2026-05-21-antigravity-cli-now-on-homebrew.md ends here)
