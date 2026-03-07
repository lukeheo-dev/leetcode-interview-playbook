# LC 0021 — Merge Two Sorted Lists

[LeetCode — Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

## Pattern
Linked List

## Problem Summary
You are given the heads of two sorted linked lists.

The goal is to merge them into one sorted linked list and return the head of the merged list.

A very important point is that the input shown by LeetCode, such as `[1,2,4]`, is only a serialized display format. Inside the function, the actual input is not a Python list. It is a `ListNode` head.

That means this problem is not about array indexing. It is about walking through nodes with `.next`.

## Approach
The key idea is to compare only the current nodes of the two lists.

Because both lists are already sorted, we do not need nested loops or all-pairs comparison. At each step:

1. Compare `current1.val` and `current2.val`
2. Link the smaller node to the result
3. Move the chosen pointer forward
4. Move the output `tail` forward
5. When one list ends, attach the rest of the other list

To make the implementation clean, use a dummy node.

- `dummy` keeps the fixed starting point of the merged list
- `tail` always points to the last node in the merged list

At the end, the real answer starts at `dummy.next`.

This problem also helped clarify an important Python idea:

- `current = current.next` means variable reassignment
- `tail.next = current1` means object mutation

So the solution is really about relinking existing nodes, not copying values into brand-new nodes.

## Code
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next

    class Solution:
        def mergeTwoLists(self, list1, list2):
            dummy = ListNode()
            tail = dummy

            current1 = list1
            current2 = list2

            while current1 and current2:
                if current1.val <= current2.val:
                    tail.next = current1
                    current1 = current1.next
                else:
                    tail.next = current2
                    current2 = current2.next

                tail = tail.next

            if current1:
                tail.next = current1
            else:
                tail.next = current2

            return dummy.next

## Complexity
- Time: O(n + m)
- Space: O(1)

## Key Takeaways
- LeetCode's displayed input like `[1,2,4]` is not the actual runtime type.
- The real input is a `ListNode` head, so traversal is done with `.next`.
- In a sorted merge, only the two current nodes need to be compared.
- A dummy node removes special-case handling for the first output node.
- `tail.next = node` is the core linked-list connection pattern.
- This problem is about rewiring nodes, not merging arrays.
