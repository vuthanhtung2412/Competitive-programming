# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # idea in order traverse the binary tree and keep track of count
    # apply pruning to save space
    curr = k
    res = -1

    def visit(node):
        if node:
            nonlocal curr
            nonlocal res
            visit(node.left)
            if res != -1:
                return
            curr -= 1
            if curr == 0:
                res = node.val
                return

            visit(node.right)

    visit(root)

    return res
