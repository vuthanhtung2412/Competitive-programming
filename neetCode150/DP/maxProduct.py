from typing import List


def maxProduct(nums: List[int]) -> int:
    # monotonic stack (absolute value) reset everytime we meet a 0
    # curMax, curMin compared accumulated product with the current number
    # we need to keep track of the min because it might be valuable when we meet a negative number
    # if the curMax is negative we discontinue the accumulation
    # need to keep track of accumulated value (which have largest abs value), the accumulated value which have largest value
    # which kind of value we need to store ?
    # res : largest product ever recorded
    res = nums[0]
    curMin = 1
    curMax = 1

    for num in nums:
        if num == 0:
            curMin = 1
            curMax = 1
            if res < 0:
                res = 0

        tmp = curMax * num
        curMax = max(num, tmp, curMin * num)
        curMin = min(num, tmp, curMin * num)
        if res < curMax:
            res = curMax

    return res
