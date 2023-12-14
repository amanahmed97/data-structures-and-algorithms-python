"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]



Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.


"""
from typing import *

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2

        return dummy.next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        l1 = list1
        l2 = list2

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            elif l2.val < l1.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        while l1:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        while l2:
            tail.next = l2
            l2 = l2.next
            tail = tail.next

        return head.next

    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        # smaller val first list to be merged into
        if list1.val <= list2.val:
            l1p = list1
            l2p = list2
        else:
            l1p = list2
            l2p = list1
        head = l1p

        l1c = l1p.next
        l2c = l2p

        # len <2
        if not l1c:
            l1p.next = l2c
            return l1p
        # elif not l2c.next:
        #     l1p.next = l2c
        #     return l1p

        while l1c and l2c:
            if l1c.val < l2c.val:
                # continue on list1
                l1p = l1c
                l1c = l1c.next
            else:
                # elif l1.val >= l2.val:
                # connect nodes l1 to l2 to l1
                # l1t = l1c.next
                l1p.next = l2c
                l2t = l2c.next
                l2c.next = l1c
                # traverse
                l1p = l1c
                l1c = l1c.next
                l2c = l2t

        while l1c:
            l1p = l1c
            l1c = l1c.next
        l1p.next = l2c
        while l2c:
            l2p = l2c
            l2c = l2c.next

        return head




