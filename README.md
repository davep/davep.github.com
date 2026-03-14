# blog.davep.org

## Introduction

This is the source for my blog, located at
[blog.davep.org](https://blog.davep.org/). All
[posts](https://github.com/davep/davep.github.com/tree/main/content) are
written in Markdown and the site itself is generated using
[BlogMore](https://github.com/davep/blogmore).

## Layout

The layout of this repository is as follows:

### Blog posts

All blog posts live inside [`posts`](./content/posts/). For the sake of
convenience they're further broken down into years. Each file is a markdown
file prefixed with the date of the post (simply to make it easier to see
them in the filesysatem in the order they were written, at least to the
granularity of date) and the rest of the filename is the slug that will be
used for the resulting post on the hosted blog.

### Pages

Assorted pages (that aren't blog posts) are written under
[`content/pages`](./content/pages/). All these pages will end up in the root
of the hosted blog.

### Attachments

Lots of posts have "attached" images, both inline and also cover images.
These are held in a date-based hierarchy under
[`extras/attachments`](./content/extras/attachments).

### Other files

While attachments are mentioned above, they're really just part of the
[extras](https://blogmore.davep.dev/setting_up_your_blog/#the-extras-directory).
The content of the [`extras`](./content/extras/) directory is copied in its
entirety to the root of the hosted blog. So in there you'll also find things
like `robots.txt`, `humans.txt`, etc.

[//]: # (README.md ends here)
