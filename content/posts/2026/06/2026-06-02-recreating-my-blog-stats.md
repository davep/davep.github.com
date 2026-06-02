---
title: Recreating my blog stats
date: 2026-06-02 17:01:42+0100
category: Tech
tags: BlogMore, Blogging, jq, JSON
---

## Introduction

Having [recently added the `dump` command to
BlogMore](/2026/05/29/blogmore-v2-33-0.html) I've been thinking I should try
and learn a little more about [`jq`](https://jqlang.org/). It's one of those
tools that's been on my radar for ages, which I've used on very rare
occasions to get something done quickly, but which I've never really used in
anger.

So I thought it might be fun to see about recreating some of the stats from
the [stats page](/stats/) using `jq` alone. Well, I say "alone", I mean
*"from the JSON data that is produced by [the BlogMore `dump`
command](https://blogmore.davep.dev/command_line/#dump-command)"*, and of
course that makes it easier given it dumps some of the key calculated
values. In other words I won't be using `jq` to calculate the word count, or
reading time, or GFI, etc.

## Post count

To start with, working out the number of posts in my blog is simple enough:

```sh
jq '. | length'
```
```json
371
```

## Category count

Getting the list of categories would be:

```sh
jq '[.[] .safe_category] | unique'
```
```json
[
  "ai",
  "coding",
  "creative",
  "emacs",
  "gaming",
  "life",
  "meta",
  "music",
  "python",
  "tech",
  "til"
]
```

and so getting the count of them is simple enough:

```sh
jq '[.[] .safe_category] | unique | length'
```
```json
11
```

## Tags count

Getting the count of tags takes a little more work, as [`safe_tags` is a
list too](https://blogmore.davep.dev/command_line/#output-properties), so I
start out with a list of lists, which I need to flatten first.

```sh
jq '[.[] .safe_tags] | flatten | unique | length'
```
```json
224
```

This, right away, is an interesting finding. In my [stats page](/stats/), as
of the time of writing, the number of tags is reported as 243, but here I'm
getting 224. Given I'm using the `safe_tags` property, which ensures all
similar tags end up with the same value (so `Hello World`, `hello world`,
and all variations, become `hello-world`), that would suggest the stats page
*isn't* taking that into account. That's [an issue to
address](https://github.com/davep/blogmore/issues/580).

## A date/time interlude

Here's where things get a little interesting for a moment. In the output of
the `dump` command from [BlogMore](https://blogmore.davep.dev/), the dates
of the posts are given in [ISO 8601
format](https://en.wikipedia.org/wiki/ISO_8601); specifically the date and
time with offset format. From what I can tell, while `jq` does have some
date/time parsing support, it can't handle that format specifically.

This means that if I try:

```sh
jq '.[0] .date | fromdate'
```

I just get:

```
jq: error (at <stdin>:27293): date "2015-06-18T14:53:00+01:00" does not match format "%Y-%m-%dT%H:%M:%SZ"
```

After some searching around it seems the only approach I can really take is
to drop the timezone offset and pretend every time is a `Z` time:

```sh
jq '.[0] .date[:19] + "Z" | fromdate'
```
```json
1434639180
```

From here I can then get a fully-parsed list of date/time values using `gmtime`:

```sh
jq '.[0] .date[:19] + "Z" | fromdate | gmtime'
```
```json
[
  2015,
  5,
  18,
  14,
  53,
  0,
  4,
  168
]
```

This isn't ideal for what I'd like to do, it's going to skew some of the
values related to time, but it's close enough for experimenting.

## Posts per year

Now that I have a way of breaking the posting time into a workable array of
values, getting the number of posts per year becomes:

```sh
jq -r '[.[] .date[:19] + "Z" | fromdate | gmtime[0]] | group_by(.) | .[] | "\(.[0]): \(length)"'
```
```
2015: 32
2016: 26
2017: 7
2018: 1
2019: 15
2020: 23
2022: 11
2023: 49
2024: 19
2025: 11
2026: 177
```

Although, to be fair to `jq`, that's kind of long-winded when I could just
pull the year itself out of the posting time:

```sh
jq -r '[.[] .date[:4]] | group_by(.) | .[] | "\(.[0]): \(length)"'
```

## Posts by month

At this point getting the posts by month of year seems obvious too:

```sh
jq -r '[.[] .date[5:7]] | group_by(.) | .[] | "\(.[0]): \(length)"'
```
```
01: 14
02: 12
03: 53
04: 57
05: 76
06: 33
07: 25
08: 25
09: 13
10: 29
11: 19
12: 15
```

## Posts by weekday

For this, I need to go back to the more involved version of the posting date
handling query, where I use [`gmtime`](https://jqlang.org/manual/#dates) to
break down the time. It turns out that the penultimate value is the day of
the week as a number. So, while it's not quite as readable in that I don't
have day names, I can get the values:

```sh
jq -r '[.[] .date[:19] + "Z" | fromdate | gmtime[-2]] | group_by(.) | .[] | "\(.[0]): \(length)"'
```
```
0: 48
1: 54
2: 51
3: 48
4: 56
5: 56
6: 58
```

In this case Sunday is the first day (the `0` day here).

## Posts by hour

Getting the posts by the hour is really just a variation on the
date-chopping query used for the posts by year and the posts by month; it's
all there in the string version of the date.

```sh
jq -r '[.[] .date[11:13]] | group_by(.) | .[] | "\(.[0]): \(length)"'
```
```
00: 1
06: 1
07: 6
08: 51
09: 35
10: 32
11: 25
12: 14
13: 22
14: 24
15: 25
16: 24
17: 18
18: 9
19: 23
20: 33
21: 21
22: 6
23: 1
```

## First and last posting dates

Getting the date of the first and latest post seems nice and easy:

```sh
jq -r '[.[] .date[0:10]] | {first: min, last: max}'
```
```json
{
  "first": "2015-06-18",
  "last": "2026-06-01"
}
```

Although, from what I can tell, `jq` doesn't have anything that makes date
arithmetic easy so working out the elapsed time between the two isn't so
straightforward. It can be done, but it's not as easy as it might be with a
bit of Python code, for example. The best I could come up with was:

```sh
jq '[ .[] | .date[:19] + "Z" | fromdate ] | ((max - min) / (365.25 * 24 * 60 * 60))'
```
```json
10.95438841990519
```

For an approximate value of "year", [of
course](https://en.wikipedia.org/wiki/Leap_year).

## Word counts

From here on in many of the stats that can be pulled out from the JSON, with
`jq`, become easier to handle. Each post has a `word_count` property, so I
only need to do this:

```sh
jq -r '[.[] .word_count] | {least: min, most: max, average: (add / length)}'
```
```json
{
  "least": 24,
  "most": 2792,
  "average": 475.0700808625337
}
```

## Reading times

A post's reading time can be accessed by `reading_time`, so it's as easy to
handle as the word counts:

```sh
jq '[.[] .reading_time] | {least: min, most: max, average: (add / length)}'
```
```json
{
  "least": 1,
  "most": 11,
  "average": 1.8921832884097034
}
```

## Gunning fog index

The Gunning fog index is available as the `gfi` property so there's no work
to do to figure it out. It is, however, a floating point value and I want
counts in each integer "bucket". That can be done with
[`round`](https://jqlang.org/manual/#math).

```sh
jq -r '[.[] .gfi | round] | group_by(.) | .[] | "\(.[0]): \(length)"'
```
```
3: 1
4: 2
5: 3
6: 7
7: 30
8: 46
9: 67
10: 70
11: 75
12: 35
13: 18
14: 11
15: 1
16: 3
17: 2
```

As for working out the mean, median and mode... while I worked out the above
queries by reading the docs, experimenting, and using Gemini on occasion to
either help me understand an error message or to explain why an approach
works the way it did, I'm going to have to leave this one 100% to Gemini.
Here's its approach to using `jq` to work out those averages:

```sh
jq '
  [ .[] | .gfi | select(. != null) ] as $raw_gfi
  | [ $raw_gfi[] | round ] as $rounded_gfi
  | ($raw_gfi | length) as $count

  # 1. Mean Calculation
  | (($raw_gfi | add) / $count) as $mean

  # 2. Median Calculation
  | ($raw_gfi | sort) as $sorted_gfi
  | (if $count % 2 == 1 then
       $sorted_gfi[($count - 1) / 2]
     else
       ($sorted_gfi[($count / 2) - 1] + $sorted_gfi[$count / 2]) / 2
     end) as $median

  # 3. Mode Calculation (using the rounded values)
  | [ $rounded_gfi
      | group_by(.)
      | map({gfi: .[0], frequency: length})
      | sort_by(.frequency)
      | reverse
      | .[]
    ] as $frequencies
  | [ $frequencies[] | select(.frequency == $frequencies[0].frequency) | .gfi ] as $modes

  # Final Object Assembly
  | {
      count: $count,
      mean: $mean,
      median: $median,
      mode: $modes
    }
'
```
```json
{
  "count": 371,
  "mean": 9.908842231503396,
  "median": 9.979198312236287,
  "mode": [
    11
  ]
}
```

As of the time of writing: that's bang on what I get in the stats. Honestly
though, by this point, I think I'd be reaching for Python or something
similar to do this sort of work. For sure, I can't say if this is a good
`jq` query, if it's in any way idiomatic, or even if it's error-free. The
numbers match what BlogMore says though.

## Conclusion

This has been a useful exercise in getting to know a little more about `jq`,
and I can see myself reaching for it to do quick little jobs now that I've
finally taken some time to dive into it. As it turns out, it's also been a
useful little audit of the content of the stats page because I've even found
a bug that needs addressing; so that's a bonus.

[//]: # (2026-06-02-recreating-my-blog-stats.md ends here)
