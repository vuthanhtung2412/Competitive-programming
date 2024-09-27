from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_list_to_bst(sorted_list):
    if not sorted_list:
        return None

    mid = len(sorted_list) // 2

    root = TreeNode(sorted_list[mid])
    root.left = sorted_list_to_bst(sorted_list[:mid])
    root.right = sorted_list_to_bst(sorted_list[mid+1:])

    return root