"""
https://leetcode.com/problems/maximum-width-of-binary-tree/
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.



Example 1:

Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).

Example 2:

Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

Example 3:

Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).



Constraints:

    The number of nodes in the tree is in the range [1, 3000].
    -100 <= Node.val <= 100


"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = deque([[root, 1, 0]])
        prevNum, prevLevel = 1, 0

        while q:
            node, num, level = q.popleft()

            if level > prevLevel:
                prevLevel = level
                prevNum = num

            res = max(res, num - prevNum + 1)

            if node.left:
                q.append([node.left, 2 * num, level + 1])
            if node.right:
                q.append([node.right, 2 * num + 1, level + 1])

        return res
