---
layout: post
title: Five days with Copilot
category: Coding
tags: Python, Blogging, AI, LLM, Copilot, GitHub, BlogMore
date: 2026-02-20 12:20:00 +0000
---

## Another itch to scratch

As [I mentioned yesterday](/2026/02/19/a-new-engine.html), I've been a happy
user of [Pelican](https://getpelican.com) for a couple or so years now, but
every so often there's a little change or tweak I'd like to make that needs
diving deeper into the templates and the like and... I go *"eh, I'll look at
it some time soon"*. Another thought that often goes through my head at
those times is *"I should build my own static site generator that works
exactly how I want"* -- because really any hacker with a blog has to do that
at some point.

Meanwhile... I've had free access to [GitHub
Copilot](https://github.com/features/copilot) attached to [my GitHub
account](https://github.com/davep) for some time now, and I've hardly used
it. At the same time, the past few months especially, I've been watching the
rise of agents as coding tools, as well as the rise of advocates for them.
Worse still, I've seen people I didn't expect to be advocates for giving up
on coding turning to these tools and suddenly writing rationales in favour
of them.

So, suddenly, the idea popped into my head: I should write my own static
site generator that I'll use for my blog, and I should try and use GitHub
Copilot to write 100% of the code, and documentation, and see how far I get.

The requirements were going to be pretty straightforward:

- It should be a static site generator that turns Markdown files into a
  website.
- It should be blog-first in its design.
- It should support non-blog-post pages too.
- It should be written in Python.
- It should use Jinja2 for templates.
- It should have a better archive system than I ever got out of my Pelican
  setup.
- It should have categories, tags, and all the usual metadata stuff you'd
  expect from a site where you're going to share content from.

Of course, the requirements would drift and expand as I went along and I had
some new ideas.

## Getting started

To kick things off, I created my repo, and then opened Copilot and typed out
a prompt to get things going. Here's what I typed:

> Build a blog-oriented static site generation engine. It should be built in
> Python, the structure of the repository should match that of my preferences
> for Python projects these days (see https://github.com/davep/oldnews and
> take clues from the makefile; I like uv and ruff and Mypy, etc).
>
> Important features:
>
> - Everything is written in markdown
> - All metadata for a post should come from frontmatter
> - It should use Jinja2 for the output templates

As you can see, I rather than get very explicit about every single detail, I
wanted to start out with a vague description of what I was aiming for. I did
want to encourage it to try and build a Python repository how I normally
would, so I pointed it at [OldNews](https://github.com/davep/oldnews) in the
hope that it might go and comprehend how I go about things; I also
doubled-down in the importance of using `uv` and `mypy`.

The result of this was... [actually
impressive](https://github.com/davep/blogmore/pull/1). As you'll see in that
PR, to get to a point where it could be merged, there was some
back-and-forth with Copilot to add things I hadn't thought of initially, and
to get it to iron out some problems, but for the most part it delivered what
I was after. Without question it delivered it faster than I would have.

Some early issues where I had to point out problems to Copilot included:

- The order of posts on the home page wasn't obvious to me, and absolutely
  wasn't reverse chronological order.
- Footnotes were showing up kinda odd.
- The main index for the blog was showing just posts titles, not the full
  text of the article as you'd normally expect from a blog.

Nothing terrible, and it did get a lot of the heavy lifting done and done
well, but it was worth noting that a lot of dev-testing/QA needed to be done
to be confident about its work, and doing this picked up on little details
that are important.

### An improvement to the Markdown

As an aside: during this first PR, I quickly noticed a problem where [I was
getting this error when generating the site from the
Markdown](https://github.com/davep/blogmore/pull/1#issuecomment-3904192942):

```
Error generating site: mapping values are not allowed in this context
  in "<unicode string>", line 3, column 15
```

I just assumed it was some bug in the generated code and left Copilot to
work it out. Instead it came back and educated me on something: [I actually
had bad YAML in the frontmatter of some of my
posts](https://github.com/davep/blogmore/pull/1#issuecomment-3904197313)!

This, by the way, wouldn't be the last time that Copilot found an issue with
my input Markdown and so, having used it, improved my blog.

### A major feature from a simple request

Another problem I ran into quickly was that previewing the generated site
wasn't working well at all; all I could do was browse the files in the
filesystem. So, almost as an offhand comment, in the initial PR, [I
asked](https://github.com/davep/blogmore/pull/1#issuecomment-3904205550):

> Can we get a serve mode please so I can locally test the site?

Just like that, it went off [and wrote a whole server for the
project](https://github.com/davep/blogmore/pull/1/changes/3449eec9b4df88e66eec0f6bba4369926ff1389e).
While the server did need a lot of extra work to really work well[^1] the
initial version was good enough to get me going and to iterate on the
project as a whole.

## The main workflow

Having kicked off the project and having had some success with getting
Copilot to deliver what I was asking for, I settled into a new but also
familiar workflow. Whereas normally, when working on a personal project,
I'll write an issue for myself, at some point pick it up and create a PR,
review and test the PR myself then merge, now the workflow turned into:

- Write an issue but do so in a way that when I assign it to Copilot it has
  enough information to go off and do the work.
- Wait for Copilot to get done.
- Review the PR, making change requests etc.
- Make any fixes that are easier for me to fix by hand that describe to
  Copilot.
- Merge.

In fact, the first step had some sub-steps to it too, I was finding. What I
was doing, more than ever, was writing issues like I'd write sticky notes:
with simple descriptions of a bug or a new feature. I'd then come back to
them later and flesh them out into something that would act as a prompt for
Copilot I found myself doing this so often I ended up adding a "Needs
prompt" label to my [usual set of issue
labels](https://github.com/davep/setup-standard-labels).

All of this made for an efficient workflow, and one where I could often get
on with something else as Copilot worked on the latest job (I wasn't just
working on other things on my computer; sometimes I'd be going off and doing
things around the house while this happened), but... it wasn't fun. It was
the opposite of what I've always enjoyed when it comes to building software.
I got to dream up the ideas, I got to do the testing, I got to review the
quality of the work, but I didn't get to actually lose myself in the flow
state of coding.

One thing I've really come to understand during those 5 days of working on
BlogMore was I *really* missed getting lost in the flow state. Perhaps it's
the issue to PR to review to merge cycle I used that amplified this, perhaps
those who converse with an agent in their IDE or in some client application
keep a sense of that (I might have to try that approach out), but this feels
like a serious loss to me when it comes to writing code for personal
enjoyment.

## The main problems

TODO: Main problems I found.

### The far-too-subordinate issue

### The yes-man issue

### The tries-too-hard issue

[^1]: Amusingly I [uncovered another
    bug](https://github.com/davep/blogmore/issues/117) while writing this
    post.

[//]: # (2026-02-20-five-days-with-copilot.md ends here)
