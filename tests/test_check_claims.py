from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = ROOT / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import check_claims


def test_read_text_file_handles_repo_unicode_docs() -> None:
    content = check_claims.read_text_file(str(ROOT / "primitives" / "circuit-breaker.mdx"))

    assert "Circuit Breaker" in content
    assert "→" in content
