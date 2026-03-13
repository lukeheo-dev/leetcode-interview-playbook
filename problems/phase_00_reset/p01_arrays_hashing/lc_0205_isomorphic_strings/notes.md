# LC 0205 — Isomorphic Strings

[LeetCode — Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

## Pattern
Arrays & Hashing (Two-Way Mapping)

## Problem Summary
Given two strings `s` and `t`, determine whether they are **isomorphic**.

Two strings are isomorphic if:
- characters in `s` can be replaced to get `t`
- the same character must always map to the same character
- two different characters cannot map to the same character

So the real requirement is a **1:1 mapping** between characters.

## Example
### True
    s = "egg"
    t = "add"

Mapping:
    e -> a
    g -> d

This is valid, so the answer is `True`.

### False
    s = "foo"
    t = "bar"

At first:
    f -> b
    o -> a

Later:
    o -> r

Now `o` is trying to map to two different characters, so the answer is `False`.

## Core Idea
This problem is not about counting or sorting.
It is about whether the mapping relationship stays consistent.

There are two separate rules to check:

### 1) Same source character must always map to the same target character
Bad case:
    o -> a
    o -> r

That breaks consistency.

### 2) Two different source characters cannot map to the same target character
Bad case:
    a -> x
    b -> x

That breaks the 1:1 mapping.

This is why checking only one direction is not enough.

## My Approach
The cleanest solution is to maintain **two dictionaries**:

- `s -> t`
- `t -> s`

That way:
- the first dictionary checks consistency from source to target
- the second dictionary prevents many-to-one collisions

This makes the logic direct and easy to reason about.

## Final Code
    class Solution:
        def isIsomorphic(self, s, t):
            mapST = {}
            mapTS = {}

            for a, b in zip(s, t):
                if a in mapST and mapST[a] != b:
                    return False

                if b in mapTS and mapTS[b] != a:
                    return False

                mapST[a] = b
                mapTS[b] = a

            return True

## Why This Works
For every character pair `(a, b)`:
- if `a` was already mapped before, it must still map to `b`
- if `b` was already mapped before, it must still come from `a`

If either rule breaks, return `False` immediately.

If the loop ends without conflict, then every character relationship was consistent in both directions, so the strings are isomorphic.

## Step-by-Step Example
Input:
    s = "paper"
    t = "title"

Process:
- `p -> t`
- `a -> i`
- `p -> t` again, still valid
- `e -> l`
- `r -> e`

Reverse side is also consistent:
- `t -> p`
- `i -> a`
- `l -> e`
- `e -> r`

No collision, so result is `True`.

Now compare with:
    s = "badc"
    t = "baba"

Process:
- `b -> b`
- `a -> a`
- `d -> b`

But `b` is already mapped back to `b`, not `d`.
So this breaks the reverse mapping rule and returns `False`.

## Complexity
- Time: `O(n)`
- Space: `O(1)` in practice for fixed character set, otherwise `O(k)` where `k` is distinct characters

The strings are scanned once, and dictionary lookups are average `O(1)`.

## What I Learned
### 1) One-way mapping is not enough
At first glance, checking only `s -> t` can feel enough.
But that misses the case where two different characters in `s` map to the same character in `t`.

So this problem is really about **bijection-style checking**, not just simple mapping.

### 2) Two dictionaries make the logic much cleaner
You could try to get clever with sets or positions, but two hash maps make the intent explicit:
- forward consistency
- reverse consistency

### 3) This is a reusable pattern
This exact structure shows up again in:
- LC 0290 — Word Pattern
- LC 0890 — Find and Replace Pattern

So this is a good pattern to remember, not just a one-off solution.

## Key Takeaways
- Isomorphic strings require **1:1 mapping**
- You must check both directions: `s -> t` and `t -> s`
- Two dictionaries are the cleanest standard solution
- This is a mapping-consistency problem, not a counting problem
