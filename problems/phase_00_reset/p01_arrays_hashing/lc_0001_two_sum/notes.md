# LC 0001 — Two Sum

LeetCode: https://leetcode.com/problems/two-sum/

## Pattern
Arrays & Hashing

## Problem Summary
Given an integer array and a target, return indices of two numbers that add up to the target. Exactly one solution exists, and you can’t reuse the same element twice.

## Approach (One-pass Hash Map)
Use a hash map `seen` to store numbers we’ve already seen and their indices.

Scan left to right:
- For current value `v`, compute `need = target - v`.
- If `need` is already in `seen`, we found the pair: return `[seen[need], i]`.
- Otherwise store `v -> i` and continue.

Why it works: for any valid pair `(i, j)` with `i < j`, when we reach `j`, the earlier value at `i` has already been stored.

## One-pass vs Two-pass (Context)
**One-pass (streaming-friendly):**
- Check complement first, then insert current value.
- Works even if data arrives over time (you don’t need the full dataset first).
- Usually preferred in interviews because it’s minimal and avoids a second loop.

**Two-pass (prebuild then search):**
- First build `value -> index` for all elements, then scan again to find complements.
- Also O(n), but requires the full dataset upfront.
- Must avoid using the same index twice (e.g., check `map[need] != i`) and be careful with duplicates overwriting indices.

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
- One-pass = “check then insert” to avoid reusing the same index.
- Two-pass is fine but needs full input and careful duplicate/index handling.
