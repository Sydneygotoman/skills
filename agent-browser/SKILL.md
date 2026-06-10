---
name: agent-browser
description: Browser automation using the agent-browser CLI (https://github.com/vercel-labs/agent-browser), a fast native Rust-based tool for AI agents. Use for navigating websites, clicking/filling/typing, taking screenshots, getting accessibility snapshots, running JS in-page, and other browser automation tasks - especially when a lightweight CLI is preferred over writing a Playwright script.
license: Complete terms in LICENSE.txt
---

# Agent Browser

CLI-driven browser automation. Each command operates on a persistent browser
session (started with `open`), so commands can be chained across multiple
invocations.

## Setup

Check if installed first:

```bash
agent-browser --version
```

If not installed:

```bash
npm install -g agent-browser
agent-browser install --with-deps   # downloads Chrome for Testing + Linux deps (first time only)
```

## Basic workflow

```bash
agent-browser open <url>          # launch browser and navigate
agent-browser snapshot            # accessibility tree with @refs - best for finding elements
agent-browser click @e2           # click by ref from snapshot
agent-browser fill @e3 "text"     # clear and fill a field
agent-browser get text @e1        # read text content
agent-browser screenshot page.png # capture screenshot
agent-browser close               # close the session when done
```

## Key commands

- **Navigation**: `open <url>`, `close`, `close --all`
- **Interaction**: `click`, `dblclick`, `fill`, `type`, `press`, `hover`, `select`, `check`, `uncheck`, `drag`, `upload`, `scroll`, `scrollintoview`
- **Inspection**: `snapshot` (accessibility tree, preferred for locating elements), `get text/html/value/attr/title/url/count/box/styles`, `is visible/enabled/checked`
- **Semantic find**: `find role <role> <action> --name <name>`, `find text <text> <action>`, `find label <label> <action> [value]`, etc.
- **Waiting**: `wait <selector>`, `wait --text "..."`, `wait --url "..."`, `wait --load networkidle`, `wait --fn "<js>"`
- **Other**: `eval <js>`, `pdf <path>`, `clipboard read/write`, `mouse move/down/up`, `batch "<cmd1>" "<cmd2>" ...`

## Tips

- Selectors can be CSS selectors, traditional locators (`#id`, `text=`), or
  `@refN` refs returned from `snapshot`/`screenshot --annotate`. Prefer
  `snapshot` to discover refs before interacting with elements.
- For dynamic apps, run `wait --load networkidle` after navigation before
  inspecting the DOM.
- Use `batch` to run multiple steps in one process invocation and reduce
  overhead.
- Run `agent-browser <command> --help` for full flag details on any command.
- Always run `agent-browser close` (or `close --all`) when finished to free
  the browser session.
