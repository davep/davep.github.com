---
layout: post
title: The switch has been made
category: Meta
tags: Python, Blogging
date: 2023-07-05 17:56:00 +0100
---

Well, it didn't take as long as I expected it to. Just [yesterday
morning](/2023/07/04/considering-pelican.html#considering-pelican) I was
giving [Pelican](https://getpelican.com/) a look over as a possible engine
for generating my blog, having wanted to move away from Jekyll for a while
now. Having tried it and liked what I saw to start with, I wrote about how I
liked it and wondered how long it would take me to make the switch.

By the evening I was making a proper effort to get the switchover started,
and just a wee while earlier, before writing this post, the switch was made!

The process of making the switch was roughly this (and keep in mind I'm
coming from using Jekyll):

1. Made a branch in the repo to work in.
2. Removed all of the Jekyll-oriented files.
3. Decided to set up Pelican and related tools in a virtual environment,
   managed using `pipenv`.
4. Ran `pelican-quickstart` to kick things off and give me a framework to
   start with.
5. Renamed the old `_posts` directory to `content`.
6. Kept tweaking the hell out of the [Pelican config
   file](https://github.com/davep/davep.github.com/blob/main/pelicanconf.py)
   until it started to look "just so" (this is a process that has been
   ongoing, and doubtless will keep happening for some time to come).
7. Tried out a few themes and settled on
   [Flex](https://github.com/alexandrevicenzi/Flex); while not *exactly*
   what I wanted, it was close enough to help keep me motivated (while
   rolling my own theme from scratch would seem fun, I just know it would
   mean the work would never get done, or at least finished).
8. Did a mass tidy up of all the tags in all the posts; something I'd never
   really paid too much attention to as the Jekyll-based blog never actually
   allowed for following tags.
9. Went though all the posts and removed double quotes from a lot of the
   titles in the frontmatter (something Jekyll seems to have stripped, but
   which Pelican doesn't).
10. Tweaked the `FILE_METADATA` to ensure that the slugs for the URLs came
    from the filenames -- by default Pelican seems to slugify the title of a
    post and this meant that some of the URLs were changing.

All in all I probably spent 6 or 7 hours on making the move; a lot of that
involving reading up on how to configure Pelican and researching themes. The
rest of it was a lot of repetitive work to fix or tidy things.

*The* most important aspect of this was keeping the post URLs the same all
the way back to the first post; as best as I can tell I've managed that.

So far I'm pleased with the result. I'm going to live with the look/theme
for a wee while and see how it sits for me. I'm sure I'll tweak it a bit as
time goes on, but at the moment I'm comfortable with how it looks.

[//]: # (2023-07-05-the-switch-has-been-made.md ends here)
