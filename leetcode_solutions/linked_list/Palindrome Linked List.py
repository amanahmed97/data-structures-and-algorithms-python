"""
https://leetcode.com/problems/palindrome-linked-list/description/

Given the head of a singly linked list, return true if it is a
palindrome
or false otherwise.



Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false



Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9


Follow up: Could you do it in O(n) time and O(1) space?
"""
from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        l, r = 0, len(stack) - 1

        while l <= r:
            if stack[l] != stack[r]:
                return False
            l += 1
            r -= 1

        return True

    def isPalindromet1(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        stack = []
        slen = 0
        flen = 0

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            slen += 1
            fast = fast.next.next
            flen += 2

        stack.reverse()
        p = 0
        print(stack)
        print(flen)
        print(slen)
        if slen % 2 != 0:
            slow = slow.next

        while slow:
            if stack[p] != slow.val:
                return False
            slow = slow.next
            p += 1

        return True


class SolutionNC:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head

        # find the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
