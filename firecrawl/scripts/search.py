#!/usr/bin/env python3
"""Search the web using Firecrawl, optionally scraping each result."""
import argparse
import os
import sys

from firecrawl import FirecrawlApp


def main():
    parser = argparse.ArgumentParser(description="Search the web with Firecrawl")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=5, help="Max results (default: 5)")
    parser.add_argument(
        "--scrape",
        action="store_true",
        help="Also scrape each result page's content as markdown",
    )
    args = parser.parse_args()

    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        sys.exit("Error: FIRECRAWL_API_KEY environment variable is not set.")

    app = FirecrawlApp(api_key=api_key)
    kwargs = {"limit": args.limit}
    if args.scrape:
        kwargs["scrape_options"] = {"formats": ["markdown"]}

    result = app.search(args.query, **kwargs)
    items = getattr(result, "data", None) or getattr(result, "web", None) or []

    for i, item in enumerate(items, 1):
        title = getattr(item, "title", "") or ""
        url = getattr(item, "url", "") or ""
        description = getattr(item, "description", "") or ""
        print(f"{i}. {title}\n   {url}\n   {description}")
        if args.scrape:
            markdown = getattr(item, "markdown", "") or ""
            if markdown:
                print("   --- content ---")
                print(markdown[:2000])
        print()


if __name__ == "__main__":
    main()
