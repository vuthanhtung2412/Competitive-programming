# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # the left node must contain p or q and the right one must contain another node
    res = root

    def containPQ(node, p, q):
        if node:
            nonlocal res
            if node.val == p:
                if containPQ(node.right, p, q)[1] or containPQ(node.left, p, q)[1]:
                    res = node
                    return True, True
                else:
                    return True, False
            elif node.val == q:
                if containPQ(node.right, p, q)[0] or containPQ(node.left, p, q)[0]:
                    res = node
                    return True, True
                else:
                    return False, True
            else:
                (lp, lq) = containPQ(node.left, p, q)
                if lp and lq:
                    return True, True
                (rp, rq) = containPQ(node.right, p, q)
                if rp and rq:
                    return True, True

                if (lp and rq) or (rp and lq):
                    res = node

                return lp or rp, lq or rq
        else:
            return False, False

    containPQ(root, p.val, q.val)
    return res
