---
title: A different approach
date: 2026-04-30 13:22:02+0100
category: AI
tags: BlogMore, Coding, Copilot, Gemini, GitHub, Google, Python, code review
cover: /attachments/2026/04/30/gemini-diff.webp
---

As mentioned in [the previous post](/2026/04/30/duplication-of-effort.html),
I've been having a play around with Copilot/Claude vs Gemini when it comes
to getting the agents to seek out "bad" code and improve it. In that first
post on the subject, I highlighted how both tools noticed some real
duplication of effort, both addressed it in more or less the same way, and
neither of them took the clean-up to its logical conclusion (or, at the very
least, neither cleaned it up in a way that I feel is acceptable).

The comparison of the two PRs
([Gemini](https://github.com/davep/blogmore/pull/426) vs [Claude via
Copilot](https://github.com/davep/blogmore/pull/427)) is going to be a slow
and occasional read, and if I notice something that catches my interest,
I'll note it on this blog.

Initially, I was looking at which files were touched by both. With Gemini it
was:

- [`content_path.py`](https://github.com/davep/blogmore/pull/426/changes#diff-ca5e941617c3b9a8d18556da79f6fc1a400c37ae04ea1ab96efff195b60185fd)
- [`generator.py`](https://github.com/davep/blogmore/pull/426/changes#diff-9bcd414441be257b448351de586a6d3c43436bc613dd542e404d8c7f080bd24a)
- [`pagination_path.py`](https://github.com/davep/blogmore/pull/426/changes#diff-5a5ec66899ab350bb8d841c129fe67d4dde77b17a55d8d24af583a02049d8693)
- [`parser.py`](https://github.com/davep/blogmore/pull/426/changes#diff-9efe9541885322ac1491d0a7c47d29a9b3dabe129227199a95c8056907b81b97)
- [`renderer.py`](https://github.com/davep/blogmore/pull/426/changes#diff-29ac7d19a2c8f6766a2fd48d76cbf6cc40216eb43b9cd32d751d9c93818377f0)
- [`utils.py`](https://github.com/davep/blogmore/pull/426/changes#diff-403ab488e41682972adf6ba09e3ed2a92de5812d8338b95112a8dd75bf0296f0)

And with Copilot/Claude:

- [`markdown/first_paragraph.py`](https://github.com/davep/blogmore/pull/427/changes#diff-e1865709216be5988af59605690d590acd5544e63f95b4df6b85f9b0d755b448)
- [`comment_invite.py`](https://github.com/davep/blogmore/pull/427/changes#diff-fcabf04c8545cb76d4000f86e286ab4325e6a55eae20f0b9441c57129c57bb40)
- [`content_path.py`](https://github.com/davep/blogmore/pull/427/changes#diff-ca5e941617c3b9a8d18556da79f6fc1a400c37ae04ea1ab96efff195b60185fd)
- [`feeds.py`](https://github.com/davep/blogmore/pull/427/changes#diff-4193670647dc0d7b85a7ac81afbde4954cb2e46d0216e0e6abac33f49d2459b4)
- [`pagination_path.py`](https://github.com/davep/blogmore/pull/427/changes#diff-5a5ec66899ab350bb8d841c129fe67d4dde77b17a55d8d24af583a02049d8693)
- [`parser.py`](https://github.com/davep/blogmore/pull/427/changes#diff-9efe9541885322ac1491d0a7c47d29a9b3dabe129227199a95c8056907b81b97)
- [`post_path.py`](https://github.com/davep/blogmore/pull/427/changes#diff-2dd82dfd583162734cc70424abd703859cb283038ed1d9e4220fd50d5c60a9e0)
- [`utils.py`](https://github.com/davep/blogmore/pull/427/changes#diff-403ab488e41682972adf6ba09e3ed2a92de5812d8338b95112a8dd75bf0296f0)

On the surface, it looks like Claude might have done a better job of finding
untidy issues in the code. Of course a proper read/assessment of the outcome
is needed to decide which is "better"; not to mention the application of a
lot of personal taste.

So, with the initial/surface impression that "Claude went deeper", I took a
look at the first file they had in common: `content_path.py`. This is
documented as a module related to:

> Shared path-resolution utilities for content output paths.
>
> This module provides the generic building blocks used by `page_path` and
> `post_path`. Each content type supplies its own allowed-variable set and
> variable dict; this module handles the common validation, substitution,
> and safety checks.

There's 3 functions in there:

- `validate_path_template` -- for validating a format string used in
  building a path.
- `resolve_path` -- given a template and some values to populate variables
  in the template, create a path.
- `safe_output_path` -- helper function for joining paths and ensuring they
  don't escape the output directory.

These seem like sensible functions to have in here, and I can imagine me
writing a similar set in terms of the problem they seek to solve.

Both agents seemed to agree on what needed some work:
`validate_path_template`. Both also seem to agree that building knowledge of
which variable is required into the function itself isn't terribly flexible;
I feel this is a reasonable review of the situation. However, the two agents
seem to disagree on how this should be resolved.

Claude's take on this is that the function should grow an optional keyword
argument called `required_variable`, which defaults to `slug`. It also adds
an `assert` to test if the required variable exists in the
`allowed_variables` (okay, I could quibble about this but given this is a
code-check rather than a user-input check, eh, I can go with it). Finally it
does the check using the new variable and also makes the error reporting a
touch more generic too.

```diff
--- /Users/davep/content_path.py        2026-04-30 13:20:00.737955197 +0100
+++ src/blogmore/content_path.py        2026-04-30 13:20:04.560178727 +0100
@@ -17,13 +17,15 @@
     template: str,
     config_key: str,
     allowed_variables: frozenset[str],
-    item_name: str,
+    item_name: str = "",
+    *,
+    required_variable: str | None = "slug",
 ) -> None:
     """Validate a path format string for a content type.

     Checks that *template* is non-empty, well-formed, references only
-    variables from *allowed_variables*, and includes the mandatory
-    ``{slug}`` placeholder.
+    variables from *allowed_variables*, and (when *required_variable* is
+    not ``None``) includes the mandatory placeholder.

     Args:
         template: The path format string to validate.
@@ -33,11 +35,19 @@
             template.
         item_name: The human-readable name of the content type used in
             the uniqueness error message (e.g. ``"page"`` or ``"post"``).
+            Ignored when *required_variable* is ``None``.
+        required_variable: The variable name that must appear in the
+            template, or ``None`` if no variable is mandatory.  Defaults
+            to ``"slug"`` for backward compatibility.

     Raises:
         ValueError: If the template is empty, malformed, references an
-            unknown variable, or omits the ``{slug}`` placeholder.
+            unknown variable, or omits the required placeholder.
     """
+    assert required_variable is None or required_variable in allowed_variables, (
+        f"required_variable {required_variable!r} is not in allowed_variables"
+    )
+
     if not template:
         raise ValueError(f"{config_key} must not be empty")

@@ -61,9 +71,9 @@
             + f". Allowed variables are: {', '.join(sorted(allowed_variables))}"
         )

-    if "slug" not in field_names:
+    if required_variable is not None and required_variable not in field_names:
         raise ValueError(
-            f"{config_key} '{template}' must contain the {{slug}} variable so that "
+            f"{config_key} '{template}' must contain the {{{required_variable}}} variable so that "
             f"each {item_name} can be uniquely identified"
         )
```

Gemini, on the other hand, has a very similar idea but allows for the fact
that the caller might want to specify multiple required variables. So in
this case it adds `required_variables` (as a positional/keyword argument
rather than a pure-keyword argument) and defaults it to a `frozenset` that
contains `"slug"`. The rest of the change is also about making the test for
the required variables, and the reporting of the error, generic. It
*doesn't* do anything about checking that the required variables are within
the allowed variables.

```diff
--- /Users/davep/content_path.py        2026-04-30 13:20:00.737955197 +0100
+++ src/blogmore/content_path.py        2026-04-30 14:47:41.607748447 +0100
@@ -18,12 +18,13 @@
     config_key: str,
     allowed_variables: frozenset[str],
     item_name: str,
+    required_variables: frozenset[str] = frozenset({"slug"}),
 ) -> None:
     """Validate a path format string for a content type.

     Checks that *template* is non-empty, well-formed, references only
-    variables from *allowed_variables*, and includes the mandatory
-    ``{slug}`` placeholder.
+    variables from *allowed_variables*, and includes the
+    *required_variables*.

     Args:
         template: The path format string to validate.
@@ -33,10 +34,13 @@
             template.
         item_name: The human-readable name of the content type used in
             the uniqueness error message (e.g. ``"page"`` or ``"post"``).
+        required_variables: The set of variable names that MUST appear
+            in the template to ensure uniqueness. Defaults to
+            ``{"slug"}``.

     Raises:
         ValueError: If the template is empty, malformed, references an
-            unknown variable, or omits the ``{slug}`` placeholder.
+            unknown variable, or omits a required variable.
     """
     if not template:
         raise ValueError(f"{config_key} must not be empty")
@@ -61,10 +65,12 @@
             + f". Allowed variables are: {', '.join(sorted(allowed_variables))}"
         )

-    if "slug" not in field_names:
+    missing = required_variables - set(field_names)
+    if missing:
         raise ValueError(
-            f"{config_key} '{template}' must contain the {{slug}} variable so that "
-            f"each {item_name} can be uniquely identified"
+            f"{config_key} '{template}' must contain the "
+            + ", ".join(f"{{{v}}}" for v in sorted(missing))
+            + f" variable(s) so that each {item_name} can be uniquely identified"
         )
```

For the most part I think I prefer what Gemini is trying to do, although
Claude's sanity check that the required variable is one of the possible
variables makes sense. I kind of feel like both of them missed the point
when it came to handling the fact that `"slug"` is required: given that
`validate_path` is otherwise built to be pretty generic, I think I would
have defaulted to nothing and simply left it up to the caller to be explicit
that `"slug"` is required, because that matters in context of the caller.
This feels like a pretty obvious case of a "business logic" vs "generic
utility code" separation of concerns scenario.

As [mentioned in passing in another
post](/2026/04/26/but-is-the-code-that-bad.html), it's interesting to see
that neither of them noticed the opportunity to turn this:

```python
unknown = set(field_names) - allowed_variables
if unknown:
    ...
```

into this:

```python
if unknown := (set(field_names) - allowed_variables):
    ...
```

I know [at least one person](https://darren.codes/) who would be happy about
this fact.

So where does this leave me? At the moment I'm not inclined to merge either
PR, but that's mainly because I want to carry on reading them and perhaps
writing some more notes about what I encounter. What this does illustrate
for me is something we know well enough anyway, but which I wanted to
experiment with and see for myself: the initial implementation of any
working code written by an agent seems optimised for that particular
function or method, perhaps class if you're lucky. It will happily repeat
the same code to solve similar problems, or perhaps even use very different
approaches to solve the same problem. What it won't do well is recognise
that this problem is solved elsewhere and so either use that other code by
calling it, or perhaps modify it slightly to make it more generic and more
applicable in more situations.

On the other hand, it *has* shown that with a bit of prompting (and keep in
mind that the prompt that arrived at this comparison was really quite vague)
it is possible to get an agent to "consider" the problem of duplication and
boilerplate and to try and address that.

Having seen the two solutions on offer here, it's hard not to conclude that
the best solution would be for me to take the PRs as flags marking places in
the code that could be cleaned up, and do the tidy myself.

At least I have, as of the time of writing, 1,380 tests to check that I've
not broken anything when I do hand-clean the code. But, hmm, there's a
question: can I *actually* trust those tests? It's not like *I* wrote them.

Guess that's a whole other thing to worry about at some point...

[//]: # (2026-04-30-a-different-approach.md ends here)
