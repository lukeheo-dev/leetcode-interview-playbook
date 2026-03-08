# LC 0242 — Valid Anagram

[LeetCode — Valid Anagram](https://leetcode.com/problems/valid-anagram/)

## Pattern
Arrays & Hashing (Frequency Counting)

## Problem Summary
Given two strings `s` and `t`, return `True` if `t` is an anagram of `s` (same characters with the same counts). Otherwise return `False`.

## My First Idea
My first instinct was to build a frequency map for each string:
- key = character
- value = how many times it appears
Then compare the two maps.

That direction was correct. The real friction was remembering how to update a Python dict safely.

## What I Got Stuck On
This line fails when the key doesn’t exist yet:

    count[ch] += 1

So I had to re-lock the mental model:

- if key exists → increment
- else → initialize to 1

Two equivalent ways:

    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

or (compact):

    count[ch] = count.get(ch, 0) + 1

`get(ch, 0)` just means “use 0 when the key is missing”.

## Final Code
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            dic_s = {}
            dic_t = {}

            for ch in s:
                if ch in dic_s:
                    dic_s[ch] += 1
                else:
                    dic_s[ch] = 1

            for ch in t:
                if ch in dic_t:
                    dic_t[ch] += 1
                else:
                    dic_t[ch] = 1

            return dic_s == dic_t

## Complexity
- Time: O(n) to build counts (dict compare is O(k), k = distinct chars)
- Space: O(k) (worst-case O(n))

## Key Takeaways
- Anagram check is fundamentally **frequency counting**, not `set()` comparison.
- `set()` removes duplicates, so it cannot represent counts.
- `count()`-based solutions can look fast for small alphabets, but scale worse in theory.
- Dict updates (`in` / `get`) are the actual “Python skill checkpoint” in this problem.
