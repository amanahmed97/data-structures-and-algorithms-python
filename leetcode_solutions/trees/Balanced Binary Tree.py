"""
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is
height-balanced
.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true



Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -104 <= Node.val <= 104
"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        d = 0

        def dfs(root):
            nonlocal d
            if root is None:
                return 0

            l, r = dfs(root.left), dfs(root.right)
            diff = abs(l - r)
            if diff > 1:
                d += diff

            return 1 + max(l, r)

        dfs(root)
        return False if d else True


