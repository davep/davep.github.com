---
title: "Trouble with PyPI"
date: "2026-06-11 16:26:06+0100"
category: Python
tags: [PyPI, Python]
cover: "/attachments/2026/06/11/pypi-500.webp"
---

I had quite the adventure with PyPI this morning, and I don't think it's
over yet. It started out with the release of [BlogMore
v2.43.0](/2026/06/11/blogmore-v2-43-0.html). I did my usual thing of doing
[a test release](https://test.pypi.org/project/blogmore/) to [the test
version of PyPI](https://test.pypi.org/), and then did a [production
release](https://pypi.org/project/blogmore/).

As normally happens, I then went on to [tag the release on
GitHub](https://github.com/davep/blogmore/releases/tag/v2.43.0), followed by
writing the blog post to announce the new version. While doing this, despite
the fact that it wasn't necessary given the nature of the change, I decided
to update BlogMore [in my blog's
repository](https://github.com/davep/davep.github.com). That's when things
started to look odd.

I did the usual [`make
update`](https://github.com/davep/davep.github.com/blob/main/Makefile) but
nothing new appeared. Now, it's not unheard of that I do this and no new
version of BlogMore appears. Often I do it a couple more times and it's
fine. So I kept trying every minute or two and still nothing. So I checked
back on PyPI. Sure enough, a search showed that it had updated:

![PyPI search](/attachments/2026/06/11/pypi-search.webp#centre)

(The 16 minutes being about the time since I'd made the release), but when I
clicked through it was showing the last version from a couple of days ago.
Even when I looked at the [release
history](https://pypi.org/project/blogmore/#history) it was saying the
latest version was the previous version:

![The apparent latest release](/attachments/2026/06/11/release-history.webp#centre)

Odd.

At this point, depending on how I searched and where I went, I'd either see
that my latest upload wasn't available, or I'd get a 500 error.

![PyPI 500 error](/attachments/2026/06/11/pypi-500.webp#centre)

Clicking through to [the status page](https://status.python.org/) showed no
errors. Clicking through to [the Twitter account that was
suggested](https://x.com/PythonStatus) showed nothing at all.

![PyPI status on Twitter](/attachments/2026/06/11/pypi-twitter.webp#centre)

Leaving aside the whole issue of having an account on Twitter these days
anyway, I felt it wasn't that useful to point people at a resource that
seems to have never been updated, [so I did raise an issue about
that](https://github.com/pypi/warehouse/issues/20145).

Digging around the status page at some point, despite the fact that the main
display was green all the way, I did see a rise in *"PyPI CDN Edge Errors"*.
I'm not a web guy, I'm not an infrastructure guy, so I'm not really sure
what this would mean, but it sounds like it's not a good thing.

![CDN edge errors](/attachments/2026/06/11/pypi-edge-errors.webp#centre)

Opening the graph to look longer term, it did seem today was a spike, with
another spike quite some time ago.

![More CDN edge errors](/attachments/2026/06/11/pypi-more-edge-errors.webp#centre)

At this point I left it a while, not announcing the new version of
[BlogMore](https://blogmore.davep.dev/). I came back some time later and,
finally, I could see 2.43.0 was showing! Also, this seemed to coincide with
the above graph calming down again.

![A calm CDN](/attachments/2026/06/11/pypi-cdn-calm.webp#centre)

Seeing this I went to upgrade BlogMore in my blog's repo/venv and this time
it all worked.

Yay!

At that point I left it alone and went about my work day. However, I don't
think whatever is going on is over. Despite the fact that it was showing
BlogMore as being v2.43.0 earlier today, once things were settled, I just
checked again as I started to write this and:

![Old BlogMore again](/attachments/2026/06/11/pypi-old-blogmore.webp#centre)

The search index on PyPI shows it as having been updated about 8 hours ago
(as I write this), but the page itself shows that the latest version is from
2 days ago. At least installing it gives me 2.43.0:

```sh
$ uv add blogmore
Using CPython 3.13.1
Creating virtual environment at: .venv
Resolved 17 packages in 325ms
Installed 16 packages in 41ms
 + blogmore==2.43.0
 + feedgen==1.0.0
 + jinja2==3.1.6
 + lxml==6.1.1
 + markdown==3.10.2
 + markupsafe==3.0.3
 + minify-html==0.18.1
 + pillow==12.2.0
 + pygments==2.20.0
 + python-dateutil==2.9.0.post0
 + python-frontmatter==1.3.0
 + pyyaml==6.0.3
 + rcssmin==1.2.2
 + rjsmin==1.2.5
 + six==1.17.0
 + watchdog==6.0.0
```

Also: [PISpy](https://github.com/davep/pispy) sees 2.43.0 as the latest
version too (something it wasn't seeing during the height of the issues this
morning).

It's all kind of confusing though.

Guess it's time for me to read up on CDN edge errors or something...

[//]: # (2026-06-11-trouble-with-pypi.md ends here)
