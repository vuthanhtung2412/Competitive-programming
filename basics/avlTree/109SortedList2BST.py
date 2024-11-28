# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
#         pass


# ROTATION Cases for AVL Tree
# LL Case: Both the node and its left child are left-heavy.
# Fix: Right rotation.

# RR Case: Both the node and its right child are right-heavy.
# Fix: Left rotation.

# LR Case: The node is left-heavy, and its left child is right-heavy.
# Fix: Left rotation on the child, then right rotation on the node.

# RL Case: The node is right-heavy, and its right child is left-heavy.
# Fix: Right rotation on the child, then left rotation on the node.

class AVLNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None 

    def insert(self, node: AVLNode):
        pass

    def delete(self, node: AVLNode):
        pass

    def getBalance(self, node):
        pass

    def rotL(self, node : AVLNode):
        pass

    def rotR(self, node : AVLNode):
        pass
    
    