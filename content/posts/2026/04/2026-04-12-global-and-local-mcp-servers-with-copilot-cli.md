---
title: Global and local MCP servers with Copilot CLI
date: 2026-04-12 11:51:13+0100
category: TIL
tags: AI, Coding, Copilot, GitHub, LLM, MCP
---

This morning I'm tinkering some more with
[NGMCP](/2026/04/11/ngmcp-an-mcp-experiment.html). Having done a release
yesterday and tested it out by globally installing it with:

```sh
uv tool install ngmcp
```

I was then left with the question: how do I easily test the version of the
code I'm working on, when I now have it set up globally? Having done the
global installation I had `~/.copilot/mcp-config.json` looking like this:

```json
{
  "mcpServers": {
    "ngmcp": {
      "command": "ngmcp",
      "args": [],
      "env": {
        "NGMCP_GUIDE_DIRS": "/Users/davep/Documents/Norton Guides"
      }
    }
  }
}
```

whereas before it looked like this:

```json
{
  "mcpServers": {
    "ngmcp": {
      "command": "uv",
      "args": ["run", "ngmcp"],
      "env": {
        "NGMCP_GUIDE_DIRS": "/Users/davep/Documents/Norton Guides"
      }
    }
  }
}
```

But now I want both. Ideally I'd want to be able to set up an override for a
specific server in a specific repository. I did some searching and reading
of the documentation and, from what I can tell, there's no method of doing
that right now[^1]. So I've settled on this:

```json
{
  "mcpServers": {
    "ngmcp-global": {
      "command": "ngmcp",
      "args": [],
      "env": {
        "NGMCP_GUIDE_DIRS": "/Users/davep/Documents/Norton Guides"
      }
    },
    "ngmcp-local": {
      "command": "uv",
      "args": ["run", "ngmcp"],
      "env": {
        "NGMCP_GUIDE_DIRS": "/Users/davep/Documents/Norton Guides"
      }
    }
  }
}
```

and then in Copilot CLI I just use the `/mcp` command to `enable` one and
`disable` the other. It's kind of clunky, but it works.

[^1]: I did see the suggestion that you can write your MCP server so that it
    does a non-response depending on the context, but that seems horribly
    situation-specific and wouldn't really help in this case anyway because
    I want it to work in both contexts, depending on what I'm doing.

[//]: # (2026-04-12-global-and-local-mcp-servers-with-copilot-cli.md ends here)
