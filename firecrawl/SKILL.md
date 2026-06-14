---
name: firecrawl
description: Scrape, crawl, and search websites and turn them into clean Markdown/JSON using the Firecrawl API (https://firecrawl.dev). Use this skill when the user asks to scrape a webpage, crawl a site, extract structured data from a URL, or search the web and pull page content. Requires a FIRECRAWL_API_KEY environment variable.
---

# Firecrawl

Turn websites into LLM-ready data using the [Firecrawl](https://firecrawl.dev) API.

## Setup

Requires the `FIRECRAWL_API_KEY` environment variable to be set (get a key at https://firecrawl.dev).
A key can be stored in `firecrawl/.env` (gitignored) as `FIRECRAWL_API_KEY=...` and loaded with
`export $(cat firecrawl/.env | xargs)` before running the scripts below.

Install the Python SDK if not already available:

```bash
pip install firecrawl-py
```

## Quick Start

### Scrape a single URL

```bash
python scripts/scrape.py "https://example.com"
```

Outputs the page content as Markdown to stdout. Use `-o FILE` to write to a file instead, and `--format html|markdown|links|screenshot` to change the output format.

### Crawl a whole site

```bash
python scripts/crawl.py "https://example.com" --limit 20
```

Crawls the site (following links up to `--limit` pages) and writes each page's Markdown to `output_dir/` (default: `./firecrawl_output`).

### Search the web

```bash
python scripts/search.py "query terms" --limit 5
```

Returns search results, optionally with scraped page content for each result (`--scrape`).

## Notes

- All scripts read the API key from `FIRECRAWL_API_KEY`.
- For large crawls, prefer a small `--limit` first to confirm the site structure before scaling up.
- Firecrawl handles JavaScript-rendered pages, so it works on sites that plain HTTP requests can't render correctly.
