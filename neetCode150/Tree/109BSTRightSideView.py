from collections import deque
from typing import List, Optional
import unittest
from parameterized import parameterized
from helperFunc import TreeNode, level_order_to_tree

class Test(unittest.TestCase):
    @parameterized.expand([
        [[1,2,3,None,5,None,4], [1,3,4]],
        [[1,None,3], [1,3]],
        [[], []]
    ])
    def test_level_order(self, list, expected):
        self.assertEqual(Solution.rightSideView(self,level_order_to_tree(list)), expected)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root : 
            return []
        res = list()
        q = deque([root])
        while q :
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if i == l-1:
                    res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return res

if __name__ == '__main__':
    unittest.main()