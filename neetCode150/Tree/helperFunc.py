from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_to_tree(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = [root]
    i = 1

    while i < len(level_order):
        current = queue.pop(0)

        if i < len(level_order) and level_order[i] is not None:
            current.left = TreeNode(level_order[i])
            queue.append(current.left)
        i += 1

        if i < len(level_order) and level_order[i] is not None:
            current.right = TreeNode(level_order[i])
            queue.append(current.right)
        i += 1

    return root
