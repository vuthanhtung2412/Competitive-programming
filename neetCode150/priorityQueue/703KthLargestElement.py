from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pq = []
        self.k = k
        for n in nums:
            if len(self.pq) < k :
                heapq.heappush(self.pq, n)
                continue
            if self.pq[0] < n :
                heapq.heappop(self.pq)
                heapq.heappush(self.pq, n) 
        pass
        

    def add(self, val: int) -> int:
        if len(self.pq) < self.k :
            heapq.heappush(self.pq, val)
        elif self.pq[0] < val :
            heapq.heappop(self.pq)
            heapq.heappush(self.pq, val) 
        return self.pq[0]