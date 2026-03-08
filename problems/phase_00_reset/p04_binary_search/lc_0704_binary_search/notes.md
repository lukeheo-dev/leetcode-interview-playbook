# LC 0704 — Binary Search

[LeetCode — Binary Search](https://leetcode.com/problems/binary-search/)

## Pattern
Binary Search

## Problem Summary
Given a sorted array `nums` and an integer `target`, return the index of `target` if it exists; otherwise return `-1`. The intended runtime is **O(log n)**.

## My Initial Thought
I understood the high-level idea (“keep cutting the search space in half”), but my first mental model was slightly wrong:
- I thought binary search was mainly “move `mid` left/right”
- The correct mindset is “shrink the range, then recompute `mid`”

That’s why updates like `start = mid` / `end = mid` felt natural at first, but they can repeat the same state and stall the loop.

## Approach (Lower Bound Style)
I used a **lower bound** style binary search:
- If `nums[mid] < target`, discard the left half including `mid` → `start = mid + 1`
- Otherwise, keep the left half including `mid` → `end = mid`
- When the loop ends, `start` is the leftmost possible position for `target`
- Finally, verify `nums[start] == target`

This is slightly different from the classic `while left <= right` template, but it’s clean and avoids off-by-one traps.

## Code
    from typing import List


    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            start = 0
            end = len(nums) - 1

            while start < end:
                mid = (start + end) // 2

                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid

            if nums[start] == target:
                return start
            return -1

## Complexity
- Time: O(log n)
- Space: O(1)

## Key Takeaways
- Binary search is about **managing a shrinking range**, not “moving `mid`”.
- Always update boundaries so the range strictly shrinks (`mid + 1` vs `mid`).
- Lower bound style gives a consistent “final check” pattern.
