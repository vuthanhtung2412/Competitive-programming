from typing import List
# Ideas : 
# l = 0, r = len(heights)-1 
# Larger width is better
# Larger height is better
# Area is limited by height of the shorter wall so we lift it first
def maxArea(height: List[int]) -> int:
    # Make the smaller pointer larger and check condition to update final result
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
