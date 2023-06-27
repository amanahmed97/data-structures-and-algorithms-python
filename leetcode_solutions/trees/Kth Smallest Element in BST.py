"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3



Constraints:

    The number of nodes in the tree is n.
    1 <= k <= n <= 104
    0 <= Node.val <= 104



Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

"""
from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root:
                return root.val

            val = list()
            val.append(root.val)

            if root.left:
                val += dfs(root.left)
            if root.right:
                val += dfs(root.right)

            return val

        res = dfs(root)
        print(res)
        res.sort()
        # return res[len(res)-k]
        return res[k - 1]
