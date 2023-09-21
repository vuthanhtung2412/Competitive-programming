# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    res = 0
    def maxDepth(node: Optional[TreeNode]) -> int:
        if node:
            ld = maxDepth(node.left)
            rd = maxDepth(node.right)
            nonlocal res
            if res < ld + rd:
                res = ld + rd
            return 1 + max(rd,ld)
        else:
            return 0
    return res