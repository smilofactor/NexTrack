"""
This test will enforce import rules for domain.
Domain is never to import any NexTrack packages.
"""

import ast
from pathlib import Path

FORBIDDEN_IMPORTS = {"services", "infrastructure", "tests"}

DOMAIN_PATH = Path("domain")


def test_domain_has_no_outward_dependencies():
    for pyfile in DOMAIN_PATH.rglob("*.py"):
        tree = ast.parse(pyfile.read_text())

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for name in node.names:
                    root = name.name.split(".")[0]
                    assert root not in FORBIDDEN_IMPORTS, \
                        f"{pyfile} imports forbidden module '{root}'"

            if isinstance(node, ast.ImportFrom):
                if node.module:
                    root = node.module.split(".")[0]
                    assert root not in FORBIDDEN_IMPORTS, \
                        f"{pyfile} imports forbidden module '{root}'"
