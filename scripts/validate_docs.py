#!/usr/bin/env python3
"""Validate that every page reference in docs.json resolves to an existing file."""

import json
import os
import sys


def collect_pages(obj, pages=None):
    """Recursively collect all page references from docs.json navigation."""
    if pages is None:
        pages = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "pages":
                if isinstance(value, list):
                    for item in value:
                        if isinstance(item, str):
                            pages.append(item)
                        elif isinstance(item, dict) and "page" in item:
                            pages.append(item["page"])
            else:
                collect_pages(value, pages)
    elif isinstance(obj, list):
        for item in obj:
            collect_pages(item, pages)
    return pages


def main():
    # Resolve repo root relative to this script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    docs_json_path = os.path.join(repo_root, "docs.json")

    if not os.path.exists(docs_json_path):
        print("ERROR: docs.json not found")
        return 1

    with open(docs_json_path) as f:
        data = json.load(f)

    pages = collect_pages(data)
    # Deduplicate
    pages = sorted(set(pages))

    missing = []
    for page in pages:
        # Check for .mdx, .md, or directory
        candidates = [
            os.path.join(repo_root, page + ".mdx"),
            os.path.join(repo_root, page + ".md"),
            os.path.join(repo_root, page),
        ]
        if not any(os.path.exists(c) for c in candidates):
            missing.append(page)

    print(f"Total page references: {len(pages)}")
    if missing:
        print(f"MISSING pages ({len(missing)}):")
        for m in missing:
            print(f"  MISSING: {m}")
        return 1
    print("All page references resolve to existing files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
