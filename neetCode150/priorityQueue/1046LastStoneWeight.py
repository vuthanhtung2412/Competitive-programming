from typing import List
import unittest
from parameterized import parameterized
import heapq

class Test(unittest.TestCase):
    @parameterized.expand([
        [[2,7,4,1,8,1], 1],
        [[1], 1],
        [[9,3,2,10],0]
    ])
    def test_level_order(self, stones, expected):
        self.assertEqual(Solution.lastStoneWeight(self,stones), expected)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-s for s in stones]
        heapq.heapify(pq)
        while len(pq) >= 2 :
            s1,s2 = heapq.heappop(pq), heapq.heappop(pq)
            if s1 != s2:
                heapq.heappush(pq,s1-s2)

        if pq:
            return abs(pq[0])
        return 0
            

if __name__ == '__main__':
    unittest.main()