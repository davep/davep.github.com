---
title: A stroppy agent
date: 2026-05-03 09:59:45+0100
category: AI
tags: BlogMore, Coding, Copilot, Gemini, GitHub, Google, Python, code review
cover: /attachments/2026/05/03/better-naming.webp
---

One of the things I noticed when I started on the [BlogMore
experiment](/tag/blogmore/) was the fact that Copilot/Claude seemed to love
to write monolithic code. Pretty early on most of the code was landing in
just a couple of files. Once I noticed this I instructed it to break things
up and always try and be more modular. This started out in the [instructions
for
Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
but eventually I migrated the instruction to `AGENTS.md` (as seems to be the
fashion these days).

While this rule seems to have held, one file that always remained pretty
large was `generator.py`. This is, as you might guess from the name, the
main site generation code. While it does sort of make sense that it is the
pivotal body of code for the application, it doesn't follow that it *has* to
contain so much code.

So, yesterday evening, I decided to experiment by asking [Gemini
CLI](/tag/gemini/) to look over the code and tell me what it thinks. The
prompt was:

> Quite a bit of work has been done on `@src/blogmore/generator.py` to try
> and reduce duplication of effort and boilerplate. I wonder if we can do a
> little more? Please take a look over the code there and see if there is
> any more repetitive code that can be cleaned up, to make the codebase more
> maintainable.
>
> Also, the file is getting quite long. I prefer Python files to be no more
> than 1000 lines at most. Please also look at the code with a view to it
> being broken up into more logical sub-modules. Perhaps
> @src/blogmore/generator.py could turn into a `generator` directory with
> smaller modules inside it.
>
> Look over this and report back with any findings. Also, don't look for
> *anything*, look for and report back changes that will make cleaner code
> and will be impactful.

I then left it to come up with an assessment while I got on with other
things.

Its headline finding was:

> **Status:** The file is currently **2,146 lines long**, significantly
> exceeding the 1,000-line maintainability threshold. It has become a "God
> Object" that handles everything from low-level byte-copying and
> regex-based minification to high-level site orchestration.

The full assessment [has been saved to a public
gist](https://gist.github.com/davep/7b89b5070589a74a72c6a25120588367).

This seemed reasonable, so I told it to get on with the job of doing this.
I've also saved the plan it made [as a
gist](https://gist.github.com/davep/1494163d2b34206054575053b82f90df).

What is notable in the plan is the validation strategy at the end. While
there is a full suite of tests available, and while this *is* documented in
`AGENTS.md`:

```markdown
- Run the test suite after every change: `make test`.
- Any new functionality **must** have associated tests.
- If a change in behaviour makes existing tests incorrect, update those tests.
  Do not change tests purely to make them pass without a genuine reason.
- Do not delete or comment out failing tests; fix the underlying code instead.
```

the plan that Gemini arrived at seemed to concentrate only on
`test_generator.py` and `test_integration.py`.

Once the work to break up `generator.py` was done I could see it had run
those tests and it was happy with the outcome. So I did the obvious thing
and ran `make test` and, sure enough, there was a failed test (I think there
was just the one). So I said to Gemini:

> you should have run all the tests. Did you read @AGENTS.md at all?

It replied with:

> Verifying Refactor Quality: Running comprehensive quality checks as
> mandated by AGENTS.md.

and then got on with the work of fixing what had been broken.

At this point it should be noted that another instruction I have in
`AGENTS.md` is:

> Use full, descriptive names for variables, functions, and classes. Do not
> use abbreviations when the full word is readable.

I've found that Copilot/Claude has done an excellent job of sticking to this
wish. If anything I'd say at times it's got a little too carried away. But,
I'm not typing this code, I'm only reading it; making the code *very*
readable from a symbol point of view makes a lot of sense.

I swear, I can see why people sometimes fall into the trap of thinking
agents have personalities, because the next thing I see, after telling it
off for obviously not reading the rules of messing in my repo, is this:

![Single letter parameter names](/attachments/2026/05/03/single-letters.webp#centre)

Now, to be fair, my instruction does mention variables, functions, and
classes. It doesn't explicitly say "parameters", I guess. But... come on!

In all other respects though it got things fixed and I ended up with a
cleaned-up generation engine that was more modular. In review, I did find a
couple of things in its plan that I wasn't super keen on (and which I could
have pushed back on right at the planning stage, so I'd say that's on me,
not on the agent), but overall it was a workable solution.

I prompted it once more to fix the things I didn't like, which it did and
did a fine job of. As part of that prompt I did say:

> I'm seeing functions in there with single letter parameter names. Please
> keep in mind the instruction about naming things in @AGENTS.md

And it did do as it was told.

![Some better naming](/attachments/2026/05/03/better-naming.webp#centre)

As amusing as this was (really, it's so tempting to think it decided to be
stroppy after I told it to go read `AGENTS.md`), it has left me wondering
though: just how widespread is the convention of looking for and reading the
agents file? While I get that each of the command-line tools seem to have a
preference for their self-named instructions file first, it was my
understanding that in the absence of such a file `AGENTS.md` is looked for.

During the session I'm talking about here, either Gemini CLI didn't do that,
or it did and just didn't take on board the conventions I wanted it to
follow.

As for the great breakup of `generator.py`... I grabbed the assessment and
the plan that Gemini came up with, [turned it into an
issue](https://github.com/davep/blogmore/issues/442), and [set Copilot to
work on it too](https://github.com/davep/blogmore/pull/443). Despite working
off the same prompt, as it were, it came up with a *very* different
approach. So my next job is to decide which of the two I like most.

As of the time of writing, the Gemini approach to cleaning this up results
in the main `site.py` file inside the new `generator` subdirectory being 996
lines; that's just under the 1,000 line limit I tend to set myself[^1], so
close enough, but not ideal. Copilot/Claude, on the other hand, is sat at
278 lines! While the idea of Gemini was to make `site.py` a small
descriptive top-to-bottom and start-to-finish description of *how* a site is
generated, it's somehow managed to make a more verbose version; the
Copilot/Claude version looks to do a far better job of fulfilling that
intention.

Then again the Gemini version has broken the work up across 9 files, the
Copilot/Claude version across 13. Also the Copilot/Claude version has taken
a really fun and interesting approach to solving the problem that I'm kind
of digging[^2].

So now I have to decide which, if either, I'm going with.

That's probably another post.

[^1]: Although in my own projects I try and keep Python files much smaller
    than that if I can help it.
[^2]: Spoiler: mixins. ALL THE MIXINS!

[//]: # (2026-05-03-a-stroppy-agent.md ends here)
