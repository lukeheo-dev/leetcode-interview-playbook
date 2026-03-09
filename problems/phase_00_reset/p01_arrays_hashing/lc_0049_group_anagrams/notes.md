# LC 0049 — Group Anagrams

[LeetCode — Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## Pattern
Arrays & Hashing (Dictionary Grouping) + String Sorting

## Problem Summary
Given an array of strings `strs`, group the anagrams together.

Two strings are anagrams if they contain the same characters with the same counts, only in a different order. The output order does not matter.

Examples:
- `"eat"`, `"tea"`, `"ate"` belong to the same group
- `"tan"`, `"nat"` belong to the same group
- `"bat"` stays alone

## My Initial Thought
Before worrying about the final output structure, I focused on a simpler question:

> How do I recognize that two strings belong to the same group?

My early thinking was more manual:
- break strings down into characters
- compare character composition
- maybe use dictionaries to compare counts
- then try to place each string into an existing group

That direction wasn’t completely wrong, but it felt heavier than necessary because it suggests a lot of pairwise comparison.

## The Important Shift (Key Insight)
The idea that simplified everything:

> If two strings are anagrams, sorting their characters produces the same result.

Examples:
- `"eat"` → `"aet"`
- `"tea"` → `"aet"`
- `"ate"` → `"aet"`

So instead of comparing strings with each other, I can:
1) normalize each string into a stable representative key (sorted string)
2) use that key in a dictionary
3) group original strings under that key

This turns “grouping” into a clean dictionary-bucketing problem.

## My Accepted Solution
I used a dictionary where:
- key = normalized string (`"".join(sorted(st))`)
- value = list of original strings that match that key

## Code
    from typing import List


    class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            dic = {}

            for st in strs:
                key = "".join(sorted(st))
                if key in dic:
                    dic[key].append(st)
                else:
                    dic[key] = [st]

            return [dic[k] for k in dic]

## Why This Works
For each string:
- `sorted(st)` returns a list of characters in sorted order
- `''.join(...)` converts it back into a string key
- all anagrams share the same sorted key
- dictionary grouping collects them into the same bucket

So the dictionary becomes conceptually like:
- `"aet"` → `["eat", "tea", "ate"]`
- `"ant"` → `["tan", "nat"]`
- `"abt"` → `["bat"]`

Finally, returning `dic.values()` (or `[dic[k] for k in dic]`) produces the grouped lists.

## Step-by-Step Example
Input:
    ["eat","tea","tan","ate","nat","bat"]

Processing:
- `"eat"` → `"aet"` → {"aet": ["eat"]}
- `"tea"` → `"aet"` → {"aet": ["eat","tea"]}
- `"tan"` → `"ant"` → {"aet": [...], "ant": ["tan"]}
- `"ate"` → `"aet"` → {"aet": ["eat","tea","ate"], "ant": ["tan"]}
- `"nat"` → `"ant"` → {"aet": [...], "ant": ["tan","nat"]}
- `"bat"` → `"abt"` → {"aet": [...], "ant": [...], "abt": ["bat"]}

Return:
    [["eat","tea","ate"], ["tan","nat"], ["bat"]]
(order can differ)

## What I Learned
### 1) Grouping problems often need a representative key
The main win is not “grouping” itself—it's choosing the right key.

Once the key is stable, the rest becomes dictionary mechanics.

### 2) `sorted(s)` returns a list
`sorted("eat")` returns `['a','e','t']`, not a string.
So `''.join(sorted(s))` is the practical tool to convert it into a usable dictionary key.

### 3) The bigger pattern is dictionary grouping
Sorting matters here, but the reusable pattern is:
- define a stable key
- group values in a dictionary
This shows up repeatedly in hash map/string problems.

## Complexity
Let:
- `n` = number of strings
- `k` = average length of each string

For each string, sorting costs `O(k log k)`.
Across all strings:
- Time: `O(n * k log k)`
- Space: `O(n * k)` for storing grouped strings (plus keys)

## Small Note on Improvement
This approach is already correct and standard.

You can refactor for readability (e.g., `defaultdict(list)`), but the main idea stays the same:
- normalize with sorting
- group with a dictionary

## Key Takeaways
- Anagrams become identical after sorting.
- The main trick is choosing a representative key.
- Dictionary grouping beats pairwise comparison.
- `sorted()` + `join()` is a practical normalization tool.
