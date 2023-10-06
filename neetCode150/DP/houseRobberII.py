from typing import List


def rob(nums: List[int]) -> int:
    # rob(nums) = max(rob(nums[:-2])+nums[-1], rob(nums[:-1]))
    # rob(nums) = max([rob(nums.remove((i+1)%(len(nums)), (i-1)%len(nums))) for i in range(len(nums))])
    # if rob a house and remove non robbable it will a linear robbing problems
    # bottom up approach for linear problem
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    def linRob(l):
        if l:
            if len(l) == 1:
                return l[0]
            res = [0 for _ in range(len(l))]
            res[0] = l[0]
            res[1] = max(l[0], l[1])
            for i in range(2, len(l)):
                # drawing while presenting the recursive relation
                res[i] = max(res[i - 2] + l[i], res[i - 1])
                # res[i] = res[i-1] + res[i-2]
            return res[-1]
        else:
            return 0

    res = 0
    for i in range(len(nums)):
        notIncluded = [i, (i - 1) % len(nums), (i + 1) % len(nums)]
        # PROBLEM: cannot filter like this because the sequence when a node is removed is different
        tmp = nums[i] + linRob([nums[n] for n in range(len(nums)) if n not in notIncluded])
        print(notIncluded)
        if res < tmp:
            print("---")
            print(notIncluded)
            print(tmp)
            print("---")
            res = tmp

    return res


def rob1(nums: List[int]) -> int:
    # rob(nums) = max(rob(nums[:-2])+nums[-1], rob(nums[:-1]))
    # rob(nums) = max([rob(nums.remove((i+1)%(len(nums)), (i-1)%len(nums))) for i in range(len(nums))])
    # if rob a house and remove non robbable it will a linear robbing problems
    # bottom up approach for linear problem
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    def linRob(l):
        if l:
            if len(l) == 1:
                return l[0]
            res = [0 for _ in range(len(l))]
            res[0] = l[0]
            res[1] = l[1]
            for i in range(2, len(l)):
                res[i] = max(res[i - 2] + l[i], res[i - 1])
            return res[-1]
        else:
            return 0

    res = 0
    for i in range(len(nums)):
        tmp = 0
        if i == 0:
            tmp = linRob(nums[2:len(nums) - 1]) + nums[i]
        elif i == len(nums) - 1:
            tmp = linRob(nums[1:len(nums) - 2]) + nums[i]
        elif i == 1:
            tmp = linRob(nums[3:]) + nums[i]
        elif i == len(nums) - 2:
            tmp = linRob(nums[:-3]) + nums[i]
        else:
            # PROBLEM: robbing 2 linear parts != robbing these 2 parts together
            tmp = linRob(nums[:(i - 1)]) + linRob(nums[i + 2:]) + nums[i]

        if res < tmp:
            res = tmp

    return res


def rob2(nums: List[int]) -> int:
    # rob(nums) = max(rob(nums[:-2])+nums[-1], rob(nums[:-1]))
    # rob(nums) = max([rob(nums.remove((i+1)%(len(nums)), (i-1)%len(nums))) for i in range(len(nums))])
    # if rob a house and remove non robbable, robbing the other houses is a linear robbing problems
    # bottom up approach for linear problem
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    res = 0
    for i in range(len(nums)):
        a = 0
        b = 0
        p = (i + 2) % len(nums)
        while p != (i - 1) % len(nums):
            tmp = b
            b = max(a + nums[p], b)
            a = tmp
            p = (p + 1) % len(nums)

        b += nums[i]
        if res < b:
            res = b

    return res


# Neetcode solution : linRob on 2 array nums[1:] and nums[:-1]
# because we cannot rob the first and the last house together
# I haven't thought of this problem because I think if I exclude the first element the robbed house might not adjacent to the first house
# However, if Neetcode solution misses this case the chosen house must also contain the last house else it will be covered in the excluded last case
def NCrob(nums: List[int]) -> int:
    # exclude the first element
    # exclude the last element
    if len(nums) == 1:
        return nums[0]

    def linRob(l):
        a = 0
        b = 0
        for i in range(len(l)):
            tmp = b
            b = max(a + l[i], b)
            a = tmp
        return b

    print(nums[1:])
    print(nums[:-1])

    return max(linRob(nums[1:]), linRob(nums[:-1]))


print(rob2([6, 3, 10, 8, 2, 10, 3, 5, 10, 5, 3]))
