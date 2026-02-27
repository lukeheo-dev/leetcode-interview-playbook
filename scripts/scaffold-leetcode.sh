#!/usr/bin/env bash
set -euo pipefail

BASE="$(pwd)"

echo "📦 Creating LeetCode scaffold..."

# Core directories (idempotent)
mkdir -p problems
mkdir -p playbook/patterns
mkdir -p playbook/english
mkdir -p playbook/templates
mkdir -p curriculum
mkdir -p scratch
mkdir -p tests

echo "🧾 Ensuring default templates exist..."

# IMPORTANT:
# - Do NOT create any file that matches pytest discovery patterns (test_*.py / *_test.py)
#   outside of `problems/**` and `tests/**`.
# - Keep templates as *.tmpl so pytest never tries to import/collect them.

# Solution template (only create if missing)
if [[ ! -f playbook/templates/solution_template.py ]]; then
  cat > playbook/templates/solution_template.py << 'EOF'
"""
LC: {id} - {title}
Pattern: {pattern}

Approach:
-

Complexity:
- Time:
- Space:

English explanation (2~4 lines):
-
"""

from __future__ import annotations


def solve(*args, **kwargs):
    raise NotImplementedError
EOF
fi

# Test template (keep as .tmpl; only create if missing)
if [[ ! -f playbook/templates/test_template.py.tmpl ]]; then
  cat > playbook/templates/test_template.py.tmpl << 'EOF'
"""Basic test template for a LeetCode problem."""

from __future__ import annotations


def test_smoke() -> None:
    # TODO: replace with real test cases
    assert True
EOF
fi

echo "⭐ Scaffold complete in: $BASE"
echo ""
echo "Folders ensured:" 
echo "- problems/"
echo "- playbook/patterns/"
echo "- playbook/english/"
echo "- playbook/templates/"
echo "- curriculum/"
echo "- scratch/"
echo "- tests/"
