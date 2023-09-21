# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    # Conditions:
    # left and right nodes are BST
    # 1. the max left is less than node.val
    # 2. the min right is greater than node.val
    # think of which kind of info we want to pass from child node to parent node
    # min max of child node (because the child node can be on the left of one node but on the right of other)
    if root is None:
        return True
    MAX = 2 ** 31
    MIN = -2 ** 31 - 1
    res = True

    def findMinMax(node):
        if node:
            nonlocal res
            mil, mal = findMinMax(node.left)
            if not res:
                return 0, 0
            mir, mar = findMinMax(node.right)
            if not res:
                return 0, 0

            if not mal < node.val < mir:
                res = False

            return min(mil, mir, node.val), max(mal, mar, node.val)
        else:
            return MAX, MIN

    findMinMax(root)
    return res
