#!/usr/bin/env python3
"""Crawl a website using Firecrawl and save each page's content to disk."""
import argparse
import os
import re
import sys

from firecrawl import FirecrawlApp


def slugify(url: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", url).strip("_")
    return slug[:150] or "page"


def main():
    parser = argparse.ArgumentParser(description="Crawl a site with Firecrawl")
    parser.add_argument("url", help="Starting URL to crawl")
    parser.add_argument("--limit", type=int, default=10, help="Max pages to crawl (default: 10)")
    parser.add_argument(
        "--output-dir",
        default="./firecrawl_output",
        help="Directory to write crawled pages to (default: ./firecrawl_output)",
    )
    args = parser.parse_args()

    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        sys.exit("Error: FIRECRAWL_API_KEY environment variable is not set.")

    os.makedirs(args.output_dir, exist_ok=True)

    app = FirecrawlApp(api_key=api_key)
    result = app.crawl_url(args.url, limit=args.limit, scrape_options={"formats": ["markdown"]})

    pages = getattr(result, "data", None) or []
    if not pages:
        sys.exit("No pages returned from crawl.")

    for page in pages:
        metadata = getattr(page, "metadata", None) or {}
        source_url = getattr(metadata, "source_url", None) or metadata.get("sourceURL") if isinstance(metadata, dict) else None
        source_url = source_url or args.url
        markdown = getattr(page, "markdown", "") or ""

        filename = os.path.join(args.output_dir, slugify(source_url) + ".md")
        with open(filename, "w") as f:
            f.write(f"<!-- source: {source_url} -->\n\n")
            f.write(markdown)

    print(f"Crawled {len(pages)} page(s) into {args.output_dir}")


if __name__ == "__main__":
    main()
