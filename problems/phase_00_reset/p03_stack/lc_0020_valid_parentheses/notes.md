# LC 0020 — Valid Parentheses

[LeetCode — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

## Pattern
Stack

## Problem Summary
Given a string containing only `()[]{}`, determine whether it is a valid parentheses string.

A valid string must satisfy:
- Every opening bracket is closed by the same type.
- Brackets close in the correct nested order.
- No closing bracket appears without a matching opener.

## What I Was Trying to Understand
Before solving it, these were the main questions:
- How do I reject crossed cases like `([)]`?
- How do I detect leftover open brackets like `([]`?
- How do I safely handle a closing bracket when the stack is empty, such as `")("`?
- Does “correct order” basically mean stack / LIFO? Yes.

## Approach
This is a stack problem.

- Push opening brackets `([{` into a stack.
- When a closing bracket appears:
  - If the stack is empty, return `False`.
  - If the top of the stack matches the expected opening bracket, pop it.
  - Otherwise return `False`.
- After the loop, the stack must be empty.

I also added two quick guards:
- If the first character is a closing bracket, return `False`
- If the last character is an opening bracket, return `False`

These guards are optional, but they reject obvious invalid cases early.

## Code
    class Solution:
        def isValid(self, s: str) -> bool:
            opens = []

            if s[0] in "})]":
                return False
            elif s[-1] in "({[":
                return False

            for ch in s:
                if ch in "({[":
                    opens.append(ch)
                elif ch == ")":
                    if len(opens) != 0 and opens[-1] == "(":
                        opens.pop()
                    else:
                        return False
                elif ch == "]":
                    if len(opens) != 0 and opens[-1] == "[":
                        opens.pop()
                    else:
                        return False
                elif ch == "}":
                    if len(opens) != 0 and opens[-1] == "{":
                        opens.pop()
                    else:
                        return False

            return len(opens) == 0

## Complexity
- Time: O(n)
- Space: O(n)

## Key Takeaways
- “Correct order” in bracket problems usually means stack.
- Always check whether the stack is empty before reading `stack[-1]`.
- Final validation requires the stack to be empty after processing the full string.
