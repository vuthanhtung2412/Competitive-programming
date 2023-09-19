from typing import List


def findDuplicate(nums: List[int]) -> int:
    # Explain:
    # nl : length of non loop part
    # l : length of the loop
    # b : steps the turtle need to take to finish the loop after meeting the rabbit
    # turtle: t = nl + l - b
    # the turtle couldn't finish one loop because there is no way the rabbit could hop over the turtle
    # rabbit: r = nl + k*l - b
    # r = 2*t => (k-1)*l - b = nl
    s = nums[0]
    f = nums[s]

    while s != f:
        s = nums[s]
        f = nums[nums[f]]

    res = 0
    while res != s:
        s = nums[s]
        res = nums[res]

    return res