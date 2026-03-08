# LC 0217 — Contains Duplicate

[LeetCode — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

## Pattern
Arrays & Hashing (Set)

## Problem Summary
Given an integer array `nums`, return `True` if any value appears at least twice. Otherwise return `False`.

## My First Idea
My first idea was to loop and repeatedly `pop()` values, then check membership in the remaining list.

It works logically, but it has two downsides:
- It mutates the input list.
- `x in nums` is a linear scan, so doing it repeatedly becomes slow (O(n²)).

## Better Approach
Use a set.

A set cannot contain duplicates, so converting the list to a set removes duplicates automatically.
If duplicates exist, the set will be smaller than the original list.

## Final Code
    from typing import List


    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            return len(nums) != len(set(nums))

## Complexity
- Time: O(n)
- Space: O(n)

## Key Takeaways
- Set membership/insertion is O(1) on average, which enables an O(n) solution.
- `len(nums) != len(set(nums))` is the cleanest duplicate check.
- Avoid mutating inputs (like `pop()`) unless the problem allows it explicitly.
