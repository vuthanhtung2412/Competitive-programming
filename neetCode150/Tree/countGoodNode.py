# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:
    res = 0

    def visit(node, maxi):
        if node:
            if node.val >= maxi:
                nonlocal res
                res += 1
                visit(node.left, node.val)
                visit(node.right, node.val)
            else:
                visit(node.left, maxi)
                visit(node.right, maxi)

    visit(root, -1e4)

    return res