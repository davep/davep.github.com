---
layout: post
title: How not to ask for help
category: Coding
tags: free-software, foss, help
date: 2024-02-04 11:27:00 +0000
---

My association with Textual works on two levels: on the one hand, sure, it's
[currently my day job](https://www.textualize.io/about-us/); on the other
hand it's a FOSS project that I'm keen to support so *"free time me"* tries
to work with it and support others working with it too. For this reason
you'll often see me being terminally[^1] online in the Textual Discord,
trying to answer questions as they come up, every waking free moment.

Almost without exception the people who ask for help are appreciative and
ask in the spirit of wanting help and wanting to work together with whoever
is helping them to get an answer. That... that's actually quite a cool thing
to be part of. I like the sense of community that comes from someone going
*"bah I'm trying to do this thing and it isn't working PLEASE HELP!"*.

And then... well, let's just say that sometimes the odd question will crop
up that seems to be asked from a less collaborative position.

Without wanting to appear to dunk on an individual (I don't wish to), I want
to break down an example that happened yesterday. For some background, I'd
been AFK all day, [having a wonderful time in town with a
friend](https://fosstodon.org/@davep/111867694675165507), shopping,
[lunch](https://fosstodon.org/@davep/111867942313370807), a movie, that sort
of thing. A nicely-chilled day where I didn't even look at the Discord
notifications that had popped up on my watch and phone.

However, later on that evening, finally home and flopped on the sofa, I saw
a question pop up that, while lacking [any useful
detail](https://label.dev/articles/minimal-reproducible-example/) and
possibly suffering a wee bit from being [an XY
problem](https://label.dev/articles/xy-problem/), the immediate answer was
clear:

> <tt>BadIdentifier: 'test.udp_json_client-input' is an invalid id; identifiers must
contain only letters, numbers, underscores, or hyphens, and must not begin with
a number.</tt>
>
> ????????????????? a dot isn't allowed?

Like I say: it lacks context and detail, and the number of question marks
doesn't really clarify much, but the core question that seems to be at play
here is *"is it true that a full stop can't be used as part of the ID of a
widget?"*.

The answer is: no, it can't. There's a reason for that too, and if someone
were to take a step back for a moment and think about how IDs play a part in
queries and how they'd be used in a stylesheet, the reason for that might
pop out. So, to help the person asking the question walk in the direction of
the answer, I reply:

> When you come to query that how would the parser know it’s not ID “test”
> combined with a class, if dot was allowed?

Before we go on, to illustrate my point, consider this ID: `foo.bar`. When
you come to query that back, or use it in a stylesheet, how would `#foo.bar`
look? Is it a widget with the ID `foo.bar`; or is it a widget with the id
`foo` and the class `bar`?

As far as Textual's CSS is concerned, it would be the latter.

But at this point it didn't seem necessary to get into all that detail; I
like to try and assume knowledge on the part of the person asking the
question, sans any other evidence, so for the moment I'll assume a *"oh,
right, yeah, that's a damn good point"* kind of reply. Or if not, perhaps a
*"I don't quite follow, could you explain?"* reply, in which case I'm happy
to go into all the detail.

The reply was neither:

> why are element ID and classes co-mingled?
>
> this was previously allowed so your question doesn't really make sense to
> me

Now I'm confused. Asking why element IDs and classes *are* co-mingled seems
odd; but I'm used to chatting with people who don't have English as a first
language so I'm going to assume it's just a wording choice; but the latter
part is very odd: this has *never* been allowed. Or, more to the point...
without any proper context I can't really appreciate what claim is being
made here.

You see... [I did notice a bug in Textual recently, when it came to widget
IDs](https://github.com/Textualize/textual/issues/3954). Long story short:
when you set your ID for the widget in your code, no actual validation of
the ID was being done. This was an oversight [that was fixed in the latest
release](https://github.com/Textualize/textual/pull/4032).

But knowing that that's the case would be guesswork on my part; I'm also
fresh at my desk after a day out; I'm probably not quite in the
coding/Textual zone yet, so rather than try and guess half of the
conversation, it's easier to just ask the person who is asking. So I ask
them to restate the question, and give some more background.

The reply is:

> the objective is to put a string like test.udp_json_client-input as the
> label of a tab, which previously just used the ID property. from skimming
> release notes, is it better to explicitly set the label, and then assign
> something compliant for the ID separately?

Wait... what? I thought we were talking about valid widget IDs, now we're
talking about tabs and labels? Do we mean `TabbeContent` and the labels of a
`TabPane`? This is a bit different. So I'm sat there trying to figure out
this person's thought process so I can offer the help they're after and this
follows:

> okay @davep, you have a real bug. --content-tab- prefix is not ephemeral.
> if I create a tab and grab .id, that prefix comes with it, so if you save
> it for later and try to set .active, assigning .active doesn't agree that
> there is a tab --content-tab-thing
>
> so I need to de-mangle the name manually before assigning .active I guess?

Wut? Like... wut? Okay, we do seem to be talking about `TabbedContent`, I
recognise the values being mentioned here; we did some work [late on last
year](https://github.com/Textualize/textual/pull/3815) that added some
namespacing to parts of the `TabbedContent` widget in an effort to [reduce
some foot-gun
situations](https://github.com/Textualize/textual/issues/3695).

But... there's no `.` being used in the IDs as part of that; why are we now
proclaiming a bug in an unrelated PR? That's quite the leap with zero
evidence. Like... sure, I'm *all* for being alerted to bugs and fixing them,
but this doesn't seem like that.

And then there's the *"so I need to..."* conclusion that also seems to have
no connection to the original question.

Anyone who has ever done support will recognise this situation, I'm sure.
Someone has seen a problem, they've dug around a little and reached a
conclusion about what the cause is, and turns up looking for help with the
*conclusion* they've reached (very much a variant of [a XY
problem](https://label.dev/articles/xy-problem/)).

That almost never gets us where we want to go, so I do the obvious thing; I
try and reboot the question; I try and get us back to the start and try and
get some clarity; I try and encourage asking the question with zero
assumptions:

> I'm afraid I'm still not really understanding your question, as it now no
> longer seems to relate to what you very first asked. Perhaps you could
> start again, ideally with an
> [MRE](https://label.dev/articles/minimal-reproducible-example/) of what
> you're looking at and trying to do, for clarity?

I figure, whatever the problem is, it can be illustrated with like a dozen
lines of code. Also, when asking people to do this, it often actually helps
them rubber-duck their own problem. There's been plenty of times on Discord
where someone's "found a bug" in Textual, they're asked to make an MRE of
it, and they come back and go *"oh, shoot, right, I did that and realised
the bug was in my code"*. It's cool when they happens; everyone learns
something.

So... no MRE comes back, but this is the reply:

> I'm trying to fix multiple breakages in my application from some recent
> changes. Right now I can't wrap my head around what to assign a
> tabbed_content.active for it to work how it did before (where if you have
> a tab with ID sample, you can assign tabbed_content.active = "sample", but
> you can't do that anymore)

While not an MRE, I *can* work with this. It seems clear that they have a
`TabbedContent` where they have a `TabPane` with the ID `"sample"` and they
are struggling to make it the `active` tab by setting `active` to
`"sample"`. That seems hugely unlikely, this is what `TabbedContent` is all
about, I think we'd have noticed (I'm petty sure we've got unit tests that
cover this), but I'm game. I can test this. And the MRE I write will
illustrate there isn't a problem.

So I reply:

> Again, I can only suggest that you make an MRE of the issue you're seeing.
> For example, here's me making a set of tabs, the last of which has the ID
> "four", and I set the active to "four":

and provide the code:

```python
from textual.app import App, ComposeResult
from textual.widgets import TabbedContent, TabPane, Label

class TabbedContentApp(App[None]):

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("One", id="one"):
                yield Label("One")
            with TabPane("Two", id="two"):
                yield Label("Two")
            with TabPane("Three", id="three"):
                yield Label("Three")
            with TabPane("Four", id="four"):
                yield Label("Four")

    def on_mount(self) -> None:
        self.query_one(TabbedContent).active = "four"

if __name__ == "__main__":
    TabbedContentApp().run()
```

Based on what they've most-recently said is the problem, I'm confident
they'll see that this MRE is their situation in a nutshell, and we can work
out from there and figure out what the problem is they're seeing and where
this `.` in their IDs is coming from (because I'm *very* confident it isn't
coming from the work that was done on `TabbedContent`).

This is good. We're getting close to heading down a good path; I can feel
it!

I was wrong.

> https://github.com/Textualize/textual/blob/main/src/textual/widgets/_tabbed_content.py#L513
>
> there's no way you can deny you just added a metric ton of shenanigans
> with the tab ID stuff. I can't get it to work at all anymore (assigning
> .active), but yes I will either come up with an MRE or find the bug and
> let you know

So, rather than back up a wee bit, work with the MRE I wrote for them so we
can take a walk through the problem, they instead decide to tell me that the
PR I did last year (which *still* isn't implicated in any of this outwith of
them seemingly assuming it's the cause of all the issues, presented with
zero evidence that it is) was simply *"a metric ton of shenanigans"*.

No!

Stop!

This is *not* how you ask for help.

This isn't how you ask for help from a product or service you pay for. This
*really* isn't how you ask for help from a Free Software project, where the
people who are offering you help are doing so in their free time because
they want people to be able to build cool things with it.

It really isn't hard at all to show just a wee bit of respect for people's
time and willingness to try and help you.

Now... I get it. I can imagine a scenario where someone has just updated
Textual and their application suddenly starts throwing all sorts of weird
and new errors. That happens. That happened to me [on Thursday evening just
gone](https://github.com/Textualize/textual/issues/4101). But that's no
reason for approaching getting help like this.

The way to approach it is this: pin the problem dependency, perhaps publish
a new version of your application so there's no accidental update of the
dependency, then head to any of the help resources for the dependency has
and *work with people who want to help you to find the cause of the
problem*. Trust me, it'll go a lot faster if you work with them, take on
board suggestions (no matter how odd they might first appear), and really
don't call their code *"a metric ton of shenanigans"*.

The conclusion to all of this? The person asking the question eventually
found they were setting some widget's ID to an invalid ID; one with a `.` in
it. So as I suspected and wanted to walk them to: they had invalid IDs all
along and they only found out about this because ID validation was fixed.

Perhaps one day they'll retract the claim that my actually-unrelated code
that wasn't "just" released [but was from last
year](https://github.com/Textualize/textual/releases/tag/v0.46.0) is *"a
metric ton of shenanigans"*. `¯\_(ツ)_/¯`

[^1]: Geddit? GEDDIT?

[//]: # (2024-02-04-how-not-to-ask-for-help.md ends here)
