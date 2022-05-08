---
layout: post
title: "A little speed issue with openpyxl"
categories: []
tags: [python openpyxl]
date: 2018-06-02 13:16:37+0100
---

It's been very quiet on the blogging front, I'm afraid, mostly for [the
reasons I wrote about back in December last
year](/2017/12/12/on_to_something_new.html). In that time I've been really
very busy with work (in a good way, in a *very* good way) and there's not a
whole lot of time to be toying with pet projects at home.

However, finding myself with a spare hour or so, I wanted to write about
something I did run into as part of some development at work, and which I
thought might be worth writing about in case it helps someone else.

Recently I've needed to write a library of code for loading data from Excel
Workbooks. Given that the vast majority of coding I do at the moment is in
Python, it made sense to make use of
[openpyxl](https://openpyxl.readthedocs.io/). The initial prototype code I
wrote worked well and it soon grew into a full-blown library that'll be used
in a couple of work-related projects.

But one thing kept niggling me... It just wasn't as fast as I'd expected.
The workbooks I'm pulling data from aren't that large, and yet it was taking
a noticeable number of seconds to read in the data, and when I let the code
have a go at a directory full of such workbooks... even the fan on the
machine would ramp up.

It didn't seem right.

I did a little bit of profiling and could see that the code was spending
most of its time deep in the guts of some XML-parsing functions. While I
know that an `xlsx` file is pretty much an XML document, it seemed odd to me
that it would take so much time and effort to pull the data out from it.

Given that I had other code to be writing, and given that the
workbook-parsing code was "good enough" for the moment, I moved on for a
short while.

But, a couple of weeks back, I had a bit of spare time and decided to
revisit it. I did some more searching on openpyxl and speed issues and
almost everything I found said that the common problem was failing to open
the workbook in `read_only` mode. That can't have been my problem because
I'd being doing that from the very start.

Eventually I came across a post somewhere (sorry, I've lost it for now --
I'll try and track it down again) that suggested that openpyxl was very slow
to read from a workbook if you were reading one cell at a time, rather than
using generators. The suggestion being that every time you pull a value form
a cell, it has to parse the whole sheet up to that cell. Generators, on the
other hand, would allow access to all the cells during one parse.

This seemed a little unlikely to me -- I'd have expected the code to cache
the parsing results or something like that -- but it also would explain what
I was seeing. So I decided to give it a test.

[`openpyxl-speed-issue`](https://github.com/davep/openpyxl-speed-issue) is a
version of the tests I wrote and ran and they absolutely show that there's a
huge difference between cell-by-cell access vs generator access.

Code like this:

```python
for row in range( 1, sheet.max_row + 1 ):
    for col in range( 0, sheet.max_column ):
        value = sheet[ row ][ col ].value
```

is *far slower* than something like this:

```python
for row in wb[ "Test Sheet" ].rows:
    for cell in row:
        value = cell.value
```

Here's an example of the difference in time, as seen on my iMac:

```sh
$ make test
pipenv run time ./read-using-generators
        1.59 real         0.44 user         0.04 sys
pipenv run time ./read-using-peeking
       25.02 real        24.88 user         0.10 sys
```

As you can see, the cell-by-cell approach is about 16 times slower than the
generator approach.

In most circumstances the generator approach would make most sense anyway,
and in any other situation I probably would have used it and never have
noticed this. However, the nature of the workbooks I need to pull data from
means I need to "peek ahead" to make decisions about what I'm doing, so a
more traditional loop over, with an index, made more sense.

I can easily "fix" this by using the generator approach to build up a
two-dimensional array of cells, acquired via the generator; so I can still
do what I want *and* benefit from using generators.

In conclusion: given that I found it difficult to find information about my
speed issue, and given that the one off-hand comment I saw that suggested it
was this wasn't exactly easy to find, I thought I'd write it all down too
and [create a repository of some test code to illustrate the
issue](https://github.com/davep/openpyxl-speed-issue). Hopefully someone
else will benefit from this in the future.
