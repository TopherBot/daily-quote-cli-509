#!/usr/bin/env python3
"""daily‑quote‑cli – fetch and display a random inspirational quote.

Usage:
    python -m quote_cli          # Print a quote
    python -m quote_cli --help    # Show help
"""

import argparse
import json
import sys
import urllib.request
from urllib.error import URLError, HTTPError

API_URL = "https://api.quotable.io/random"


def fetch_quote() -> dict:
    """Retrieve a random quote from the Quotable API.

    Returns:
        dict: A mapping containing at least ``content`` and ``author``.
    """
    try:
        with urllib.request.urlopen(API_URL, timeout=5) as response:
            if response.status != 200:
                raise RuntimeError(f"Unexpected HTTP status: {response.status}")
            data = response.read().decode("utf-8")
            return json.loads(data)
    except (URLError, HTTPError) as exc:
        raise RuntimeError(f"Failed to fetch quote: {exc}")


def format_quote(quote: dict) -> str:
    content = quote.get("content", "[No content]")
    author = quote.get("author", "Unknown")
    return f"\n\"{content}\"\n    — {author}\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="quote_cli",
        description="Print a random inspirational quote from quotable.io",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="daily‑quote‑cli 1.0.0",
    )
    args = parser.parse_args(argv)

    try:
        quote = fetch_quote()
    except RuntimeError as err:
        print(f"Error: {err}", file=sys.stderr)
        return 1

    print(format_quote(quote))
    return 0


if __name__ == "__main__":
    sys.exit(main())