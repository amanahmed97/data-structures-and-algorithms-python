"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1

Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            def checker(root, child, p, q):
                op = list()
                ov = list()

                if not child:
                    return ov, op

                if child.val == p.val or child.val == q.val:
                    ov.append(child.val)

                l, lop = checker(child, child.left, p, q)
                r, rop = checker(child, child.right, p, q)

                ov += l
                ov += r

                if p.val in ov and q.val in ov:
                    op.append(child.val)

                if root.val == p.val or root.val == q.val:
                    ov.append(root.val)

                op += lop
                op += rop

                return ov, op

            resv, resop = checker(root, root, p, q)
            return TreeNode(resop[-1])