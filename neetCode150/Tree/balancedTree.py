# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    # conditions:
    # left and right trees are balanced
    # difference between left depth and right depth
    if root is None:
        return True

    def maxDepth(node: Optional[TreeNode]) -> int:
        if node:
            ld = maxDepth(node.left)
            rd = maxDepth(node.right)

            if ld == -1 or rd == -1 or ld - rd > 1 or ld - rd < -1:
                return -1

            return 1 + max(ld, rd)
        else:
            return 0

    return maxDepth(root) != -1

def isBalancedPruned(self, root: Optional[TreeNode]) -> bool:
    # conditions:
    # left and right trees are balanced
    # difference between left depth and right depth
    if root is None:
        return True

    def maxDepth(node: Optional[TreeNode]) -> int:
        if node:
            # stop the recursion early
            ld = maxDepth(node.left)
            if ld == -1:
                return -1

            rd = maxDepth(node.right)
            if rd == -1:
                return -1

            if ld - rd > 1 or ld - rd < -1:
                return -1

            return 1 + max(ld, rd)
        else:
            return 0

    return maxDepth(root) != -1