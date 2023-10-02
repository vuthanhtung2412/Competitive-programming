from typing import List


def maxSubArray(nums: List[int]) -> int:
    # this is a 2 pointer problems
    # if the sum of previous sub-array is negative there is no point in keeping track of them
    # update res if current sum reaches new max
    res = int(-1e4)
    curr = 0
    for num in nums:
        if curr <= 0:
            curr = num
        else:
            curr += num

        if res < curr:
            res = curr

    return res