# LC 0014 — Longest Common Prefix

[LeetCode — Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Pattern
Arrays & Hashing (String Scanning)

## Problem Summary
Find the longest prefix shared by all strings in the array. If none exists, return an empty string.

## Approach
Use vertical scanning:
- Take the first string as a reference.
- Compare characters at index `i` across all strings.
- Stop at the first mismatch or when a string ends, and return the prefix up to `i`.

This is simple, interview-friendly, and supports early exit.

## Code
    from typing import List


    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            first = strs[0]

            for i in range(len(first)):
                ch = first[i]
                for s in strs[1:]:
                    if i >= len(s) or s[i] != ch:
                        return first[:i]

            return first

## Complexity
- Time: O(N * M) where M is the minimum string length
- Space: O(1)

## Key Takeaways
- Prefix means “from index 0” — scanning from the start is the cleanest.
- Early mismatch → fast return.
- Python: be careful with indexing vs iterating characters.
