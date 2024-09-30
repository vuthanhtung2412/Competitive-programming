from collections import deque
from typing import List, Optional
import unittest
from parameterized import parameterized
from helperFunc import TreeNode, level_order_to_tree

class Test(unittest.TestCase):
    @parameterized.expand([
        [[3,9,20,None,None,15,7], [[3],[9,20],[15,7]]],
        [[1], [[1]]],
        [[], []]
    ])
    def test_level_order(self, list, expected):
        self.assertEqual(Solution.levelOrder(self,level_order_to_tree(list)), expected)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : 
            return []
        res = list()
        q = deque([root])
        while q :
            level = list()
            l = len(q)
            for _ in range(l):
                n = q.popleft()
                level.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            res.append(level)
        return res

if __name__ == '__main__':
    unittest.main()