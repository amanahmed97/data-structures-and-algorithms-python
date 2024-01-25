"""
https://leetcode.com/problems/delete-node-in-a-bst/description/

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node
reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

    Search for a node to remove.
    If the node is found, delete the node.



Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []
"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # if root.left is None and root.right is None:
            #     return None
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            cur = root.right
            while cur.left:
                cur = cur.left

            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root

    def deleteNodet1(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                tmp = root.left
                root = root.right
                if root.left is None:
                    root.left = tmp
                else:
                    root.left.left = tmp
                return root
        if root.left is None and root.right is None:
            return root

        def dfs(parent, root):
            if root is None:
                return

            if root.val == key:
                # if parent is None:
                #     tmp = root.left
                #     if root.right:
                #         root = root.right
                #     else:
                #         root = root.left
                #     # root.left = tmp
                #     return
                if parent.left.val == key:
                    parent.left = root.right
                else:
                    parent.right = root.right

                root.right.left = root.left

                return
            if key > root.val:
                dfs(root, root.right)
            else:
                dfs(root, root.left)

        dfs(None, root)
        return root
