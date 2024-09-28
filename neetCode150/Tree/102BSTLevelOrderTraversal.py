from typing import List, Optional
import unittest
from parameterized import parameterized
from helperFunc import TreeNode, sorted_list_to_bst

class Test(unittest.TestCase):
    @parameterized.expand([
        [[3,9,20,None,None,15,7], [[3],[9,20],[15,7]]],
        [[1], [[1]]],
        [[], []]
    ])
    def test_level_order(self, list, expected):
        self.assertEqual(levelOrder(sorted_list_to_bst(list)), expected)

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    return list()

if __name__ == '__main__':
    unittest.main()