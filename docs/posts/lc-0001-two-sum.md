---
title: "LC 0001 — Two Sum"
pattern: "Arrays & Hashing"
phase: "Phase 00 — Reset"
---

## Idea
Use a hash map to remember the index of numbers we've seen.
For each number `x`, check if `target - x` already exists in the map.
If yes, we found the pair.

## Complexity
- Time: O(n)
- Space: O(n)

## Python (hash map)
```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i

```

