from typing import List
def maxArea(height: List[int]) -> int:
    res = 0
    l = 0
    r = len(height) - 1
    while l < r:
        if height[l] < height[r]:
            if res < height[l] * (r - l):
                res = height[l] * (r - l)
            while l < r:
                l += 1
                if height[l] >= height[l - 1]:
                    break
        else:
            if res < height[r] * (r - l):
                res = height[r] * (r - l)
            while l < r:
                r -= 1
                if height[r] >= height[r + 1]:
                    break
    return res
