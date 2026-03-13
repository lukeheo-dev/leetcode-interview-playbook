# LC 0290 — Word Pattern

[LeetCode — Word Pattern](https://leetcode.com/problems/word-pattern/)

## Pattern
Arrays & Hashing (Bijection / Mapping Consistency)

## Problem Summary
Given a pattern string `pattern` and a string `s`, determine whether the words in `s` follow the same pattern.

This is a **bijection** problem:
- one pattern character must map to exactly one word
- one word must map to exactly one pattern character
- two different pattern characters cannot map to the same word

Example:

    pattern = "abba"
    s = "dog cat cat dog"

This is valid because:
- `a -> dog`
- `b -> cat`

## My Initial Thought
The first thing that came to mind was:

> If this is a bijection problem, maybe I can compare the number of unique things.

So I started from three kinds of uniqueness:
- unique characters in `pattern`
- unique words in `s`
- unique `(pattern_char, word)` pairs

In Python, that naturally becomes:

    set(pattern)
    set(words)
    set(zip(pattern, words))

At first, I tried a simpler version based only on unique counts of `pattern` and `words`.

## First Attempt
My early code was basically this idea:

    class Solution:
        def wordPattern(self, pattern: str, s: str) -> bool:
            return len(set(pattern)) == len(set(s.split(" "))) and len(pattern) == len(s.split(" "))

This looked reasonable at first because:
- if the number of unique pattern letters matches the number of unique words
- and the total lengths match
- maybe the mapping is valid

## The Problem With That Approach
It fails because **unique counts alone do not verify structure**.

Example:

    pattern = "aba"
    s = "dog cat cat"

This should be `False`.

Why?
- first `a -> dog`
- `b -> cat`
- then `a -> cat`

Now `a` is mapping to two different words, which breaks the rule.

But just comparing:
- `len(set(pattern))`
- `len(set(words))`

can still accidentally pass.

So the missing piece was:

> I also need to validate the actual pair structure, not just the counts.

## The Important Shift
That led to the better idea:

If the mapping is truly bijective, then these three counts must all match:

    len(set(pattern))
    len(set(words))
    len(set(zip(pattern, words)))

Why?

Because:
- `set(pattern)` counts distinct pattern symbols
- `set(words)` counts distinct words
- `set(zip(pattern, words))` counts distinct mapping pairs

If any side collapses incorrectly, the lengths stop matching.

## My Final Code
    class Solution:
        def wordPattern(self, pattern: str, s: str) -> bool:
            words = s.split(" ")

            if len(pattern) != len(words):
                return False

            return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))

## Why This Works
Take:

    pattern = "abba"
    words   = ["dog", "cat", "cat", "dog"]

Then:

    set(pattern) = {"a", "b"}
    set(words) = {"dog", "cat"}
    set(zip(pattern, words)) = {("a", "dog"), ("b", "cat")}

All three sets have size 2, so the mapping is consistent.

Now look at a bad example:

    pattern = "aba"
    words   = ["dog", "cat", "cat"]

Then:

    set(pattern) = {"a", "b"}                  -> size 2
    set(words) = {"dog", "cat"}               -> size 2
    set(zip(pattern, words)) = {("a","dog"), ("b","cat"), ("a","cat")} -> size 3

Now the sizes do not match, so the answer is `False`.

That is the exact reason the `set(zip(...))` trick works.

## Step-by-Step Intuition
This problem is very close to **Isomorphic Strings**.

The only difference is:
- in Isomorphic Strings, both sides are character-by-character strings
- here, one side is characters and the other side is words

But the core idea is the same:

> We are checking mapping consistency.

That is why both problems can be solved with:
- two hash maps
or
- a set-based bijection trick

## Interview-Style Standard Solution
In interviews, people often prefer the explicit two-dictionary version because it is easier to explain line by line:

    class Solution:
        def wordPattern(self, pattern: str, s: str) -> bool:
            words = s.split()

            if len(pattern) != len(words):
                return False

            p_to_w = {}
            w_to_p = {}

            for p, w in zip(pattern, words):
                if p in p_to_w and p_to_w[p] != w:
                    return False
                if w in w_to_p and w_to_p[w] != p:
                    return False

                p_to_w[p] = w
                w_to_p[w] = p

            return True

That version makes the bijection rule explicit:
- `pattern -> word`
- `word -> pattern`

## Why I Like the Set Solution
For Python specifically, the set-based solution is very compact and elegant.

The real insight is:

> If a bijection exists, the number of unique left items, right items, and mapping pairs must all match.

That is a very “Pythonic” way to express the relationship.

So even though the two-map solution is the standard teaching version, I think the set solution is a strong final answer in Python.

## Complexity
Let `n` be the number of words.

- Splitting the string: `O(n)`
- Building sets: `O(n)`
- Building `zip(...)` pairs and converting to a set: `O(n)`

Overall:
- Time: `O(n)`
- Space: `O(n)`

## What I Learned
### 1. Bijection is the real concept
This problem is not mainly about strings.
It is about whether two sequences can form a one-to-one mapping.

### 2. Unique count alone is not enough
Just comparing `len(set(pattern))` and `len(set(words))` misses structure errors.

### 3. `set(zip(...))` is the missing structural check
That pair set is what captures the actual mapping relationship.

### 4. This is basically the same family as Isomorphic Strings
Different surface, same pattern:
- mapping consistency
- one-to-one correspondence
- hash-based validation

## Key Takeaways
- The heart of the problem is **bijection validation**
- `set(pattern)`, `set(words)`, and `set(zip(pattern, words))` together provide a compact Python solution
- This is a close variation of **LC 0205 — Isomorphic Strings**
- In interviews, the two-dictionary solution is more explicit, but in Python the set trick is very clean
