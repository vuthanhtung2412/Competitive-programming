from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def maxPathSum(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    res = -1001

    def maxDescPath(node: Optional[TreeNode]):
        if node is None:
            return 0

        nonlocal res
        if node.left is None and node.right is None:
            if res < node.val:
                res = node.val
            return node.val

        # max() syntax
        # print(max(2, 3))
        # print(max(2, 3, 23))
        # print(max(list1))
        lv = maxDescPath(node.left)
        rv = maxDescPath(node.right)
        leafMax = max(lv, rv)
        if node.right is None:
            leafMax = lv
        elif node.left is None:
            leafMax = rv
        throughRoot = lv + rv + node.val
        root2Leaf = leafMax + node.val
        flag = max([leafMax, throughRoot, root2Leaf, node.val])

        if res < flag:
            res = flag

        if leafMax < 0:
            return node.val
        else:
            return leafMax + node.val

    maxDescPath(root)

    return res