#!/usr/bin/env bash
set -euo pipefail

BASE="$(pwd)"

echo "📦 Creating LeetCode scaffold..."

# Core directories
mkdir -p problems
mkdir -p playbook/patterns
mkdir -p playbook/english
mkdir -p playbook/templates
mkdir -p curriculum
mkdir -p scratch
mkdir -p tests

echo "🧾 Creating default templates..."

# Solution template
cat > playbook/templates/solution_template.py << 'EOF2'
\"\"\"
LC: {id} - {title}
Pattern: {pattern}

Approach:
-

Complexity:
- Time:
- Space:

English explanation (2~4 lines):
-
\"\"\"

from __future__ import annotations

def solve(*args, **kwargs):
    raise NotImplementedError
EOF2

# Test template
cat > playbook/templates/test_template.py << 'EOF3'
\"\"\"
Basic test template for a LeetCode problem
\"\"\"

from __future__ import annotations

def run_tests() -> None:
    # TODO: add test cases
    assert True

if __name__ == "__main__":
    run_tests()
    print("✅ All tests passed")
EOF3

echo "⭐ Scaffold complete in: $BASE"
echo ""
echo "Folders created:"
echo "- problems/"
echo "- playbook/patterns/"
echo "- playbook/english/"
echo "- playbook/templates/"
echo "- curriculum/"
echo "- scratch/"
echo "- tests/"
