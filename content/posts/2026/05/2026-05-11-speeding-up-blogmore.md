---
title: Speeding up BlogMore
date: 2026-05-11 12:30:25+0100
category: Coding
tags: AI, BlogMore, Coding, Gemini, Python
---

As [mentioned recently](/2026/05/09/blogmore-v2-20-0.html),
[Andy](https://www.yakshaving.co.uk/) did a nifty bit of testing of
[BlogMore](https://blogmore.davep.dev/) to [measure the performance hit of
each of the optional generation
features](https://www.yakshaving.co.uk/posts/blogmore-performance/).
Performance is something I haven't really spent much time thinking about; I
cared more about how the result looked than I did about how quickly a site
got generated.

I seem to remember that, early on, I did have a bit of a play with trying to
get Copilot to tackle the idea of parallel generation of parts of the site,
but [I didn't seem to get any sort of win out of
it](https://github.com/davep/blogmore/pull/283) so I closed the PR and gave
up on the idea.

Now though, especially having added the elapsed time of each step to the
progress report during generation, I am curious about what wins there are.
One that came to mind right away, and I have been considering dealing with
for a wee while, [is the fact that every generation downloads the
FontAwesome metadata](https://fosstodon.org/@davep/116540338542474954).
Caching that would be a simple win, for example.

But, if I'm going to do this, it makes sense that I stick to the spirit of
this project and get one or more agents to tackle the problem. So I asked
[Gemini](/tag/gemini/) CLI to look over the codebase and give me some big
easy wins. I made clear I didn't want it to do any work yet, I just wanted
it to report back what it could find.

The result made a lot of sense. Here's what it said:

<blockquote markdown="1">
## Performance Optimization Recommendations for BlogMore

I have conducted a comprehensive review of the `blogmore` codebase and
identified several areas where measurable and significant speedups can be
achieved, particularly for larger sites.

### 1. Backlink Snippet Extraction (Highest Impact)

The most significant bottleneck is in `src/blogmore/backlinks.py`. The
`build_backlink_map` function iterates through every internal link in every
post. For each link, it calls `_extract_snippet`, which **re-parses the
entire Markdown content of the source post** to generate a plain-text
snippet.

- **The Issue:** If a post has 20 internal links, it is parsed 20 times just
  for backlinks.
- **The Win:** Modify the logic to insert unique markers for *all* links in
  a post and perform a single Markdown-to-plain-text conversion per post.

### 2. Redundant Markdown Parsing for Metadata

The `Post` object in `src/blogmore/parser.py` has properties like
`description` and `reading_time` that are accessed frequently (on the post
page, index pages, RSS feeds, search index, etc.).

- **The Issue:** `Post.description` calls `extract_first_paragraph`, and
  `Post.reading_time` calls `calculate_reading_time`. Both of these
  functions perform a **full Markdown conversion** every time they are
  called because they are not cached.
- **The Win:** Use `functools.cached_property` on these fields.
  Additionally, these should be calculated by extracting text from the
  `html_content` that has already been generated during the initial parse,
  rather than re-parsing the raw Markdown.

### 3. Sequential Processing

The generator currently processes everything sequentially in a single
thread.

- **The Issue:** For a site with hundreds or thousands of posts, the initial
  Markdown parsing and the subsequent Jinja2 rendering are strictly serial,
  leaving multi-core CPUs mostly idle.
- **The Win:** Use `multiprocessing` (e.g., `ProcessPoolExecutor`) to
  parallelize the parsing of Markdown files and the rendering of HTML pages.
  Since these tasks are CPU-bound and independent, this would scale almost
  linearly with the number of CPU cores.

### 4. Asset Management Inefficiencies

The `AssetManager` in `src/blogmore/generator/assets.py` performs some
operations that could be optimized:

- **FontAwesome Metadata:** It downloads icon metadata from GitHub on
  *every* build to optimize CSS. This can be cached locally to avoid network
  latency.
- **Icon Generation:** It regenerates favicons and Apple touch icons on
  every build. This should be skipped if the source icon hasn't changed.

### 5. Minor Algorithmic Improvements

- **Navigation Lookups:** In `PageGenerator.generate_post_page`, the code
  uses `all_posts.index(post)` to find the current post's position for
  prev/next links. This is an O(N) operation called N times, leading to
  O(N^2) behavior. Pre-calculating a mapping would make this O(1).
- **Markdown Instance Reuse:** Several utility functions
  (`markdown_to_plain_text`, `extract_first_paragraph`) create a fresh
  `markdown.Markdown` instance on every call. Reusing a single instance (and
  calling `.reset()`) or caching the instance creation would reduce
  overhead.

### Summary

The "Big Wins" are definitely **optimizing backlink snippet extraction** and
**implementing parallel parsing/rendering**. Together, these would likely
reduce generation time for large sites by 60-80% on modern hardware.

</blockquote>

At first glance they all seem pretty sensible, and I like that it seems to
have found some really obvious big improvements, and also the little wins
that might have a cumulative effect. I strongly suspect the parallel
generation suggestion is again going to be a non-win (and so for now I'm
going to pass on it), but most of the other suggestions seem doable and
worth trying out.

I think what I will do, rather than work through them all in one PR, is
tackle one at a time. So, over the next few days, expect to see some PRs
turn up and get merged (hopefully), as I try and tease some speed wins out
of the code.

[//]: # (2026-05-11-speeding-up-blogmore.md ends here)
