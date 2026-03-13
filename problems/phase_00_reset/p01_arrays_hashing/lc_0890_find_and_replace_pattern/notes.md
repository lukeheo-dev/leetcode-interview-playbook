# LC 0890 — Find and Replace Pattern

[LeetCode — Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)

## Pattern
Arrays & Hashing

## Problem Summary
Given a list of strings `words` and a string `pattern`, return all words that match the same pattern.

A word matches the pattern if there is a bijection between characters in `pattern` and characters in the word.

That means:

- one pattern character maps to exactly one character
- one character maps back to exactly one pattern character
- two different pattern characters cannot map to the same character

Example:

    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = "abb"

Expected output:

    ["mee", "aqq"]

## Approach
I did not get to the final solution immediately.

This problem became easier because I had just solved **LC 290 — Word Pattern**. That earlier problem gave me a few important ideas:

- simple set-size comparison is not enough
- `zip()` is useful when comparing two sequences by index
- these problems are really about bijection
- the same mapping problem can be solved in more than one valid way

In LC 290, I first thought about comparing only the number of unique items. That was not enough, because matching counts do not guarantee a valid mapping relationship.

That pushed me toward a more structural view of pattern problems.

### First idea: normalize the pattern shape
My first natural idea for this problem was not to compare letters directly, but to convert each string into the same structural form.

For example:

    "abb" -> [0, 1, 1]
    "mee" -> [0, 1, 1]
    "aqq" -> [0, 1, 1]
    "abc" -> [0, 1, 2]
    "ccc" -> [0, 0, 0]

If two strings normalize to the same sequence, they have the same pattern shape.

That was a very useful mental breakthrough because it made me focus on structure instead of raw characters.

A normalize helper can look like this:

    def normalize(text):
        mapping = {}
        result = []
        next_id = 0

        for ch in text:
            if ch not in mapping:
                mapping[ch] = next_id
                next_id += 1
            result.append(mapping[ch])

        return result

Then the logic becomes:

    normalize(word) == normalize(pattern)

I liked this because it was intuitive and easy to reason about.

### Second idea: explicit bijection with two hash maps
After that, I wanted a more standard interview-style solution.

So I rewrote it with two dictionaries:

- `ptow`: pattern character -> word character
- `wtop`: word character -> pattern character

This is the direct bijection check.

The main realization here was that I should not blindly insert into the dictionary first. I need to check for conflicts before accepting the current pair.

For each word, I reset both dictionaries and scan with:

    for p, w in zip(pattern, word):

If both characters are unseen, I register the mapping.

If either side already exists, I verify that the old mapping is still consistent.

That is the version I chose as my submitted solution because it is more explicit about the actual bijection.

## Code
    from typing import List


    class Solution:
        def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
            answer = []

            for word in words:
                ptow = {}
                wtop = {}
                matched = True

                for p, w in zip(pattern, word):
                    if p not in ptow and w not in wtop:
                        ptow[p] = w
                        wtop[w] = p
                    else:
                        if p in ptow and ptow[p] != w:
                            matched = False
                            break
                        if w in wtop and wtop[w] != p:
                            matched = False
                            break

                if matched:
                    answer.append(word)

            return answer

## Complexity
- Time: O(N * L)
- Space: O(L)

Where:

- `N` = number of words
- `L` = length of each word

## Key Takeaways
- This problem became much clearer after solving LC 290 first.
- Set counts alone do not prove a valid mapping.
- `zip()` is the right tool for index-by-index comparison.
- Pattern problems are often about structure, not raw characters.
- I found two valid ways to think about the same problem:
  - normalize the pattern shape
  - check bijection directly with two hash maps
- The normalize approach helped my intuition.
- The two-hashmap approach felt stronger for interviews because it shows the bijection explicitly.
