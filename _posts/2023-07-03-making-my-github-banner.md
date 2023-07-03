---
layout: post
title: A new GitHub profile README
categories: []
tags: [ "GitHub", "Python", "Textual" ]
date: 2023-07-03 08:15:00 +0100
---

![](https://raw.githubusercontent.com/davep/davep/main/davep.svg)

Ever since GitHub introduced the [profile
README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)[^1]
I've had a massively low-effort one in place. I made the repo, quickly wrote
the file, and then sort of forgot about it. Well, I didn't so much forget as
just keep looking at it and thinking "I should do something better with that
one day".

Thing is, while there are lots of fancy approaches out there, and lots of
neat generator tools and the like... they just weren't for me.

Then yesterday, over my second morning coffee, after [getting my blog
environment up and going again](/2023/07/02/catching-up.html), I had an
idea. It could be cool to use [Textual's screenshot
facility](https://textual.textualize.io/api/app/#textual.app.App.save_screenshot)
to make something terminal-themed! I mean, while it's not *all* I am these
days, so much of what I'm doing right now is aimed at the terminal.

So... what to do? Then I thought it could be cool to knock up some sort of
login screen type thing; with a banner. One visit to an online large
terminal text generator site later, I had some banner text. All that was
left was to write [a simple Textual application to create the
"screen"](https://github.com/davep/davep/blob/main/make_banner.py).

The main layout is simple enough:

```python
def compose(self) -> ComposeResult:
    yield Label(NAME, classes="banner")
    yield Label(PRATTLE)
    yield Label("github.com/davep login: [reverse] [/]")
```

where `NAME` contains the banner and `PRATTLE` contains the "login message".
With some [Textual CSS](https://textual.textualize.io/guide/CSS/) sprinkled
over it to give the exact layout and colour I wanted, all that was left was
to make the snapshot. This was easy enough too.

While the whole thing isn't fully documented just yet, Textual does have [a
great tool for automatically running an application and interacting with
it](https://textual.textualize.io/api/app/#textual.app.App.run_test); that
meant I could easily write a function to load up my app and save the
screenshot:

```python
async def make_banner() -> None:
    async with GitHubBannerApp().run_test() as pilot:
        pilot.app.save_screenshot("davep.svg")
```

Of course, that needs running async, but that's simply enough:

```python
if __name__ == "__main__":
    asyncio.run(make_banner())
```

Throw in a `Makefile` so I don't forget what I'm supposed to run:

```
.PHONY: all
all:
    pipenv run python make_banner.py
```

and that's it! Job done!

From here onward I guess I could have some real fun with this. It would be
simple enough I guess to modify the code so that it changes what's displayed
over time; perhaps show a "last login" value that relates to recently
activity or something; any number of things; and then run it in a cron job
and update the repository.

For now though... I'll stick with keeping things nice and simple.

---
[^1]: It was actually kind of annoying when they introduced it because the
    repo it uses is named after your user name. I already had a `davep`
    repo: it was a private repo where I was slowly working on a (now
    abandoned, I'll start it again some day I'm sure) ground-up rewrite of
    my `davep.org` website.
