"""
https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even
indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        odd = head;
        even = head.next;
        evenhead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenhead

        return head
    def oddEvenList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []

        if head is None:
            return head

        prev = head
        curr = prev.next
        i = 2
        if curr is None:
            return head
        even.append(curr.val)
        prev = curr
        curr = curr.next
        i = 3

        while curr:
            if i % 2 == 0:
                even.append(curr.val)
            else:
                prev.val = curr.val
                prev = prev.next
            i += 1
            # prev = curr
            curr = curr.next

        llen = i - 1
        odds = llen // 2 + llen % 2

        i = 2
        prev = head
        curr = prev.next
        while curr:
            if i > odds:
                curr.val = even.pop(0)

            i += 1
            prev = curr
            curr = curr.next

        return head

