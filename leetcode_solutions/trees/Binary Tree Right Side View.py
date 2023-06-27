"""
https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=leetcode-75
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 100].
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def rightbfs(root: TreeNode, val: List[int]):
            if root is None:
                return val

            rval, lval = [], []

            if root.right:
                rval.append(root.right.val)
                rval = rightbfs(root.right, rval)
            if root.left:
                lval.append(root.left.val)
                lval = rightbfs(root.left, lval)

            # sight = []
            i = 0
            while i < len(rval):
                val.append(rval[i])
                i += 1
            while i < len(lval):
                val.append(lval[i])
                i += 1

            return val

        if root is None:
            return root
        val = [root.val]
        return rightbfs(root, val)