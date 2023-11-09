"""
https://leetcode.com/problems/rotate-list/description/
Given the head of a linked list, rotate the list to the right by k places.



Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]



Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109
"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0 or head.next is None:
            return head

        l = 0
        cur = head
        while cur:
            cur = cur.next
            l += 1

        old_head = head
        if k % l == 0:
            return head
        k %= l

        slow, fast = head, head

        while fast and fast.next:
            if k <= 0:
                slow = slow.next
            fast = fast.next
            k -= 1

        new_tail = slow
        new_head = slow.next
        fast.next = old_head

        new_tail.next = None

        return new_head