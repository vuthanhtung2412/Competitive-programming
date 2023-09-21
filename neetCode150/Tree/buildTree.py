# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if preorder:
        if len(preorder) == 1:
            return TreeNode(preorder[0], None, None)

        # search mid node in inorder list
        flag = -1
        for i in range(len(inorder)):
            if preorder[0] == inorder[i]:
                flag = i
                break

        return TreeNode(preorder[0], buildTree(preorder[1:1 + flag], inorder[0:flag]), buildTree(preorder[1 + flag:], inorder[flag + 1:]))

    else:
        return None