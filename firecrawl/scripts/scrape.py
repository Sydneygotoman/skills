#!/usr/bin/env python3
"""Scrape a single URL using Firecrawl and print/save the result."""
import argparse
import os
import sys

from firecrawl import FirecrawlApp


def main():
    parser = argparse.ArgumentParser(description="Scrape a URL with Firecrawl")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument(
        "--format",
        default="markdown",
        choices=["markdown", "html", "links", "screenshot"],
        help="Output format (default: markdown)",
    )
    parser.add_argument("-o", "--output", help="Write result to this file instead of stdout")
    args = parser.parse_args()

    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        sys.exit("Error: FIRECRAWL_API_KEY environment variable is not set.")

    app = FirecrawlApp(api_key=api_key)
    result = app.scrape_url(args.url, formats=[args.format])

    content = getattr(result, args.format, None)
    if content is None:
        content = str(result)
    if not isinstance(content, str):
        content = str(content)

    if args.output:
        with open(args.output, "w") as f:
            f.write(content)
        print(f"Saved to {args.output}")
    else:
        print(content)


if __name__ == "__main__":
    main()
