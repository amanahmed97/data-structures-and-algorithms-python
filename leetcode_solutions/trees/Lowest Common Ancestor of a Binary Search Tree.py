"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2



Constraints:

    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the BST.


"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root


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


class Tries:
    def lowestCommonAncestor6(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checker(root, child, p, q):
            op = list()
            ov = list()

            if not child:
                return ov, op

            if child.val == p.val or child.val == q.val:
                ov.append(child.val)

            l, lop = checker(child, child.left, p, q)
            r, rop = checker(child, child.right, p, q)
            for v in l:
                ov.append(v)
            for v in r:
                ov.append(v)

            if p.val in ov and q.val in ov:
                op.append(child.val)

            if root.val == p.val or root.val == q.val:
                ov.append(root.val)

            for v in lop:
                if v not in op:
                    op.append(v)
            for v in rop:
                if v not in op:
                    op.append(v)

            return ov, op

        resv, resop = checker(root, root, p, q)
        return TreeNode(resop[-1])


    def lowestCommonAncestor5(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checker(root, child, p, q):
            op = list()
            ov = list()

            if not child:
                return ov, op

            # if root.val == p.val or root.val == q.val:
            #     ov.append(root.val)
            if child.val == p.val or child.val == q.val:
                ov.append(child.val)

            l, lop = checker(child, child.left, p, q)
            r, rop = checker(child, child.right, p, q)
            for v in l:
                ov.append(v)
            for v in r:
                ov.append(v)

            if child.val == 1:
                print(ov, op)

            if p.val in ov and q.val in ov:
                # op.append((root.val,2))
                op.append((child.val, 2))
            elif p.val in ov or q.val in ov:
                op.append((child.val, 1))

            if root.val == p.val or root.val == q.val:
                ov.append(root.val)

            if child.val == 1:
                print(ov, op)

            for v in lop:
                if v not in op:
                    op.append(v)
            for v in rop:
                if v not in op:
                    op.append(v)

            if child.val == 1:
                print(ov, op)
                # print(op)
            # print(op)
            return ov, op

        resv, resop = checker(root, root, p, q)
        print(resv)
        print(resop)
        res = []
        for r in resop:
            if r[1] == 2:
                res.append(r[0])

        return TreeNode(res[-1])

    def lowestCommonAncestor4(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checker(root, p, q):
            if not root:
                return list(), list()

            op = list()
            ov = list()
            # if root.val == p.val or root.val == q.val:
            #     op.append(root)
            if root.left:
                if root.left.val == p.val or root.left.val == q.val:
                    # op.append(root.val)
                    ov.append(root.left.val)
            if root.right:
                if root.right.val == p.val or root.right.val == q.val:
                    # op.append(root.val)
                    ov.append(root.right.val)

            l, lop = checker(root.left, p, q)
            r, rop = checker(root.right, p, q)
            for v in l:
                ov.append(v)
            for v in r:
                ov.append(v)

            if p.val in ov and q.val in ov:
                op.append(root.val)
            for v in lop:
                op.append(v)
            for v in rop:
                op.append(v)
            # print(op)
            return ov, op

        res, resop = checker(root, p, q)
        if root.val == p.val or root.val == q.val:
            resop.insert(0, root.val)
        print(res)
        print(resop)
        tn = TreeNode(res[-1])
        return TreeNode(resop[-1])
        # return tn if len(res)>2 else root
        # if len(res)>1 else root

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checker(root, p, q):
            if not root:
                return list()

            op = list()
            # if root.val == p.val or root.val == q.val:
            #     op.append(root)
            if root.left:
                if root.left.val == p.val or root.left.val == q.val:
                    op.append(root.val)
            if root.right:
                if root.right.val == p.val or root.right.val == q.val:
                    op.append(root.val)

            l = checker(root.left, p, q)
            r = checker(root.right, p, q)
            for v in l:
                op.append(v)
            for v in r:
                op.append(v)

                # print(op)
            return op

        res = checker(root, p, q)
        if root.val == p.val or root.val == q.val:
            res.insert(0, root.val)
        print(res)
        tn = TreeNode(res[-1])
        return tn if len(res) > 2 else root
        # if len(res)>1 else root

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checker(root, p, q):
            if not root:
                return list()

            op = list()
            # if root.val == p.val or root.val == q.val:
            #     op.append(root)
            if root.left:
                if root.left.val == p.val or root.left.val == q.val:
                    op.append(root)
            if root.right:
                if root.right.val == p.val or root.right.val == q.val:
                    op.append(root)

            l = checker(root.left, p, q)
            r = checker(root.right, p, q)
            for v in l:
                op.append(v)
            for v in r:
                op.append(v)

                # print(op)
            return op

        res = checker(root, p, q)
        if root.val == p.val or root.val == q.val:
            res.insert(0, root)
        print(res)
        return res[-1] if len(res) > 1 else root
        # if len(res)>1 else root

    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def checker(root, p, q):
            if not root:
                return list()

            op = []
            if root.val == p.val or root.val == q.val and root.val not in op:
                op.append(root.val)

            l = checker(root.left, p, q)
            r = checker(root.right, p, q)
            for v in l:
                if v not in op:
                    op.append(v)
            for v in r:
                if v not in op:
                    op.append(v)
            print(op)
            return op

        return checker(root, p, q)