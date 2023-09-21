# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    if root:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    else:
        return 0
