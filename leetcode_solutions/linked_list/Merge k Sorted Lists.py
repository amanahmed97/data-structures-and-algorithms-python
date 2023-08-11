"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []



Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 1:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists

        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next

    def mergeLists2(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.val = l1.val
                l1 = l1.next
                tail.next = ListNode()
                tail = tail.next
            elif l1.val > l2.val:
                tail.val = l2.val
                l2 = l2.next
                tail.next = ListNode()
                tail = tail.next
            else:
                tail.val = l1.val
                l1 = l1.next
                tail.next = ListNode()
                tail = tail.next

                tail.val = l2.val
                l2 = l2.next
                tail.next = ListNode()
                tail = tail.next

        while l1:
            tail.val = l1.val
            l1 = l1.next
            tail.next = ListNode()
            tail = tail.next

        while l2:
            tail.val = l2.val
            l2 = l2.next
            tail.next = ListNode()
            tail = tail.next

        return dummy


