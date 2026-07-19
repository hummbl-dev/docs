#!/usr/bin/env python3
"""Check for stale quantitative claims in docs pages.

Flags drift-prone phrases like test counts, primitive counts, and
compliance framework claims that should be verified against source-of-record.
"""

import os
import re
import sys

# Patterns that indicate a quantitative claim needing verification
CLAIM_PATTERNS = [
    # Test counts — must match source-of-record
    (r"\b(\d+)\s+(?:passing\s+)?tests?\b", "test count claim"),
    # Primitive counts
    (r"\b(\d+)\s+governance\s+primitives?\b", "primitive count claim"),
    # "Fully complies with" — strongest claim, needs external audit
    (r"\bfully\s+compl(?:ies|iant)\s+with\b", "full compliance claim (requires external audit)"),
]

# Files to scan
SCAN_GLOBS = ["*.mdx", "README.md", "CLAIM_LEDGER.md"]

def read_text_file(filepath: str) -> str:
    """Read repository docs as UTF-8 regardless of host locale."""
    with open(filepath, encoding="utf-8") as f:
        return f.read()


def main():
    # Resolve repo root relative to this script file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    findings = []

    for root, dirs, files in os.walk(repo_root):
        # Skip hidden dirs, node_modules, and sources/ (archived external snapshots)
        dirs[:] = [d for d in dirs if not d.startswith(".") and d != "node_modules" and d != "sources"]
        for filename in files:
            if filename.endswith((".mdx", ".md")):
                filepath = os.path.join(root, filename)
                relpath = os.path.relpath(filepath, repo_root)
                content = read_text_file(filepath)
                # Skip CLAIM_LEDGER.md itself — it's the policy file, not a claim source
                if filename == "CLAIM_LEDGER.md":
                    continue
                for pattern, claim_type in CLAIM_PATTERNS:
                    for match in re.finditer(pattern, content, re.IGNORECASE):
                        line_num = content[: match.start()].count("\n") + 1
                        line = content.split("\n")[line_num - 1].strip()
                        findings.append((relpath, line_num, claim_type, line))

    if findings:
        print(f"Found {len(findings)} quantitative claim(s) requiring verification:")
        print()
        for relpath, line_num, claim_type, line in findings:
            print(f"  {relpath}:{line_num} [{claim_type}]")
            print(f"    {line[:120]}")
            print()
        print("Verify each claim against CLAIM_LEDGER.md and source-of-record repos.")
        print("If a claim is current, ensure it has an entry in CLAIM_LEDGER.md.")
        return 1 if any(f[2] == "full compliance claim (requires external audit)" for f in findings) else 0

    print("No stale quantitative claims detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
