---
layout: post
title: "Reading 2bit files (for fun)"
categories: []
tags: [ "bioinformatics" ]
date: 2020-08-30 15:20:00+0100
---

# Introduction

I've written a bit before about the value of having simple but interesting
"problems", that you know the solution to, as [a way of exercising yourself
in a new environment](/2019/11/10/going-on-a-journey.html). Recently I've
added another to the list I already have, and I used it as an excuse to get
back into writing [some Common
Lisp](https://github.com/davep/org-davep-2bit); and then went on to use it
as a reason to write [yet another]((https://elisp.dev/)) package [for
Emacs](https://github.com/davep/2bit.el).

Having gone through the process of writing code to handle 2bit files twice
in about a month, and in two very similar but slightly different languages,
I thought it might be interesting for me to then use it to exercise my
ability to write blog posts (something I always struggle with -- I find
writing *very hard* on a number of levels) and especially posts that explain
a particular problem and how I implemented code relating to that problem.

Also, because the initial version of this post rambled on a bit too much and
I lost the ability to finish it, I'm starting again and will be breaking it
up a number of posts spanning a number of days -- perhaps even weeks -- so
that I don't feel too overwhelmed by the process of writing it. I will, of
course, make sure every post links to the other posts.

Now, before I go on, I'll make the important point that everything here is
written from the perspective of a software developer who happens to work as
part of a bioinformatics team; I don't do bioinformatics, I don't claim to
understand it, I just happen to sit with (well, used to sit with them --
hopefully we'll all make it back to the office one day!) and work with them,
and develop software that supports their work. Anything you see in any of
the posts that's wrong about that subject: that's just my ignorance being
shown through the lens of a software developer (all corrections are
welcome).

So, with all those disclaimers aside, I'm going to go on a slow wander
through what a 2bit file is, how you'd go about reading it, and related
issues. This isn't designed as a tutorial or anything like that, this is
simply me taking what I've learnt and writing it down. Perhaps someone else
will benefit one day, but the purpose is to simply enjoy cementing it in my
own mind and to enjoy the process of putting it all in writing.

# What is a "2bit file"?

So what's this new "problem" I've added to my list? It's code to read
sequence data from [2bit format
files](https://genome.ucsc.edu/FAQ/FAQformat.html#format7). For anyone who
doesn't know (*bioinformatics people look away now; a software developer is
going to explain one of your file formats*), this is a file format that is
intended to hold sequences in an efficient way. As I'm sure you know,
[DNA](https://en.wikipedia.org/wiki/DNA) is made up of [4
bases](https://en.wikipedia.org/wiki/Nucleobase), represented by the letters
[`T`](https://en.wikipedia.org/wiki/Thymine),
[`C`](https://en.wikipedia.org/wiki/Cytosine),
[`A`](https://en.wikipedia.org/wiki/Adenine) and
[`G`](https://en.wikipedia.org/wiki/Guanine). So, in the simplest case, we
could just represent a genome using those four letters. Simple enough,
right? Nice big text file with just those 4 letters in?

The thing is, something like the human genome is around [3 billion bases in
length](https://en.wikipedia.org/wiki/Human_genome#Molecular_organization_and_gene_content).
That'd make for a petty big file to have to store and move around. So why
not compress it down a bit? That's where the 2bit format comes in.

Given this problem I'm sure most developers would quickly notice that, given
4 different characters, you only need 2 bits to actually hold them all (two
bits gets us `00`, `01`, `10` and `11`, so four different states). This
means with a little bit of coding you can store 4 bases in a single byte.
Just like that you've pretty much squished the whole thing down to 1/4 of
the original size. And that's more or less what the 2bit format does. If you
take a look at [the actual data for the human
genome](http://hgdownload.cse.ucsc.edu/goldenPath/hg38/bigZips/) you'll see
that `hg38.2bit` is roughly 1/4 of 3 billion bytes, ish, give or take.

There is a wrinkle, however. There are parts of a genome where you might not
know what base is there. Generally [an `N` is used for
that](https://www.bioinformatics.org/sms/iupac.html). So, actually, we want
to be able to store 5 different characters. But 5 isn't going to go into 2
bits... Damn! Well, it's okay, 2bit has a solution to that too, and I'll
cover that later on.

# How is a 2bit file formatted?

As you can see from [the format information available
online](https://genome.ucsc.edu/FAQ/FAQformat.html#format7), a 2bit file is
a binary file format that is split into 3 key parts:

- A fixed size header with some key information
- An index into the rest of the file
- A series of records that contain actual sequence information

In this first post I'll cover the details of the header. Subsequent posts
will cover the index and the actual sequence data records.

## The header

The header of a 2bit file is fixed in size and contains some key
information. It can be broken down as follows:

| Content        | Type    | Size    | Comments                     |
|----------------|---------|---------|------------------------------|
| Signature      | Integer | 4 bytes | See below for endian issues. |
| Version        | Integer | 4 bytes | Always 0.                    |
| Sequence count | Integer | 4 bytes |                              |
| Reserved       | Integer | 4 bytes | Always ignored.              |

The signature value is used to test if what you're looking at is a 2bit
file, but also tells you some vital information about how to read the file
-- see below for more on that. The version value is always `0` -- as such
another useful test would be to error out if you get a valid signature but
get a version other than `0`. The sequence count is, as you'd guess, the
number of sequences that are held within the file -- this is important when
loading in the index of the file (more on that in the next post).

## The signature, big and little endianness, and byte swapping

The header mentioned above comprises of 4 32-bit word values. The very first
word is important to how you read the rest of the file. This is the
`signature` for the 2bit file and it should always be `0x1A412743`. And this
is where it gets interesting and fun right away. The 2bit file format allows
for the fact that the file can be built in either [a little-endian or a
big-endian machine](https://en.wikipedia.org/wiki/Endianness), and the
32-bit word values can be binary-written to the file in the local
architecture's byte order. The effect of this is that, from reading the very
first value in the file, you need to decide if every other numeric value you
read needs to be byte-swapped in some way. The early logic being (in no
particular language) something like:

```
if signature == 0x1A412743 then
  must_swap = False
else if byte_swap( signature ) == 0x1A412743 then
  must_swap = True
else
  raise "This isn't a valid 2bit file"
end
```

Simply put, to read the rest of the file you will need a function that
byte-swaps a 32bit numeric value, and a flag of some sort to mark that you
need to do this every time you read such a value. Of course, depending on
your language of choice, you could do it in a number of different ways. In a
language like JavaScript or Scheme, where you can easily throw around
functions, I'd probably just assign the appropriate 32bit-word-reading
function to a global function name and call that regardless throughout the
rest of the code. In other languages I'd probably just check the flag each
time and call the swapping function if needed. In something like Python I'd
likely just use the signature to decide on which format to pass to
[`struct.unpack`](https://docs.python.org/3.8/library/struct.html#struct.unpack).
For example, some variation on:

```python
# Assuming that 'header' is the whole header of the file read as a binary buffer.

word_fmt = ""

for test_fmt in ( "<I", ">I" ):
    if struct.unpack( test_fmt, header[ 0:4 ] )[ 0 ] == 0x1A412743
        word_fmt = test_fmt
        break

if not word_fmt:
    raise Exception( "This isn't a 2bit file" )
```

Now, the Python approach sort of hides the important detail here. With it
we'd simply use `struct.unpack`'s [ability to handle different byte orders
](https://docs.python.org/3.8/library/struct.html#byte-order-size-and-alignment)
and not worry about the detail. Which isn't fun, right? So how might code to
byte-swap a 32bit value look?

Assuming you've got the value as an actual numeric integer, it can be as
simple as using a bit of bitwise anding and shifting. Here's the basic code
I wrote in Common Lisp, for example:

```lisp
(defun swap-long (value)
  "Swap the endianness of a long integer VALUE."
  (logior
   (logand (ash value -24) #xff)
   (logand (ash value -8) #xff00)
   (logand (ash value 8) #xff0000)
   (logand (ash value 24) #xff000000)))
```

JavaScript might be something like:

```js
function swapLong( value ) {
    return ( ( value >> 24 ) & 0xff       ) |
           ( ( value >>  8 ) & 0xff00     ) |
           ( ( value <<  8 ) & 0xff0000   ) |
           ( ( value << 24 ) & 0xff000000 )
}
```

and other variations on that theme in different languages.

## Up next

In [the next post](/2020/09/05/reading-2bit-files-for-fun-the-index.html)
I'll write about how the sequence index is stored and how to load it,
including some considerations about how to make the loading as efficient as
possible.

[//]: # (2020-08-30-reading-2bit-files-for-fun.md ends here)
