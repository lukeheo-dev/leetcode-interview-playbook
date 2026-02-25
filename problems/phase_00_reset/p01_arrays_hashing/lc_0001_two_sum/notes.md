# LC 0001 — Two Sum

## Pattern
Arrays & Hashing

## Problem Summary
Given an integer array and a target, return indices of two numbers that add up to the target. Exactly one solution exists, and you can’t reuse the same element twice.

## Approach
Use a hash map to store numbers we’ve already seen and their indices.

Scan left to right:
- `need = target - v`
- If `need` is already in the map, return the stored index and current index.
- Otherwise store `v -> i` and continue.

This works because for any valid pair `(i, j)` with `i < j`, when we reach `j`, the earlier value at `i` has already been stored.

## Code
    from typing import List


    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}  # value -> index

            for i, v in enumerate(nums):
                need = target - v
                if need in seen:
                    return [seen[need], i]
                seen[v] = i

## Complexity
- Time: O(n)
- Space: O(n)

## Key Takeaways
- Hash map reduces brute force O(n²) to O(n).
- “Check first, then insert” prevents using the same index twice.
- One-pass logic is stream-friendly.
