"""
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []



Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        res = []
        if root:
            q.append(root)

        while q:
            val = []
            for i in range(len(q)):
                node = q.pop(0)
                val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)

        return res

    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS trying
        def dfs(root):
            if root == None:
                return None

            op = list()
            # op.append([root.val])
            level = list()

            if root.left:
                level.append(root.left.val)
            if root.right:
                level.append(root.right.val)

            if level:
                op += [level]

            lop = self.levelOrder(root.left)
            rop = self.levelOrder(root.right)

            if lop:
                op += lop
            if rop:
                op += rop
            # if level:
            #     op+=level

            print(level, op)
            return op

        res = dfs(root)
        if root:
            res.insert(0, [root.val])
        return res

