---
layout: post
title: Considering Pelican
categories: []
tags: Python, Blogging
date: 2023-07-04 08:32:00 +0100
---

Since getting my blog editing environment set up on the "new" machine [a
couple of days back](/2023/07/02/catching-up.html) I've been thinking some
more about moving away from Jekyll. Jekyll itself has served me well since I
started this blog [back in 2015](/2015/06/18/hello-world.html), but I was
reminded again when installing it on the Mac Mini that it's Ruby-based and I
have very little understanding of how to get a good Ruby experience on
macOS[^1].

Having mentioned on Mastodon that I was thinking about finally looking at
moving my blog management/generation to something new, and specifically
something Python-based and ideally some sort of site generator, I got a few
suggestions.

One that looks promising so far as [Pelican](https://getpelican.com/). At
first glance it seems to tick a few boxes for me:

- Python-based (so easy for me to grok in terms of installing, and also more
  chance of being hackable).
- Uses Markdown (curiously as an alternative, to reStructuredText, which
  looks to be the default).
- Does article-based stuff as well as page-based stuff.
- Lots of themes, and themes are Jinja2-based (I'm pretty familiar with
  Jinja thanks to my Django days and also [using the library when kicking
  off `ng2web`](https://github.com/davep/ng2web)).
- RSS feed generation.
- Syntax-highlighted code blocks.


While I'm not quite ready to dive in and make the move just yet (I am on a
"muck about at home" holiday this week, but I've got enough planned without
losing a day to rebooting my blog), I did do a quick experiment to see if
Pelican would work for me.

Key to this is can I keep the URLs for all the posts the same? If I can't
that's a non-starter.

Things got off to a good start with an easy install:

```sh
$ pipx install "pelican[markdown]"
```

I then used the `pelican-quickstart` to kick off a test site, copied in my
existing Markdown files, dived into the docs and found how to configure the
generated URLs and... yeah, within like 10 minutes I had a *very* rough
version of my blog up and going.

It looked like garbage, the theme really wasn't to my taste at all, but the
core of the blog was working.

I've nuked it all for now but a more considered evaluation is now on my TODO
list. Things I'll need to drive into properly are:

- Find a base theme that's to my taste.
- Get Disqus working it so that any old comments remain in place.
- Get my image/attachment layout back in place.
- Go through and tidy up all the tagging (which has been a mess with this
  blog because I never did get round to getting Jekyll to actually use
  tags).
- Figure out the best way to do the publishing to GitHub pages.
- Likely a bunch of other stuff I've not thought about yet.

But, yeah, for a brief "over first coffee of the day" tinker to see if I
like it... I like!

Let's see how long it takes me to actually get around to making the switch.
;-)

---
[^1]: When setting this up a couple of days back, I had to pin some packages
    for the blog to older versions because of Ruby version issues; I'm sure
    that Ruby has virtual environment solutions akin to Python, but diving
    into that just for one tool... nah.
