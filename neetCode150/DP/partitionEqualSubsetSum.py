from typing import List


def canPartition(nums: List[int]) -> bool:
    # res = reduce(or, [find(s-num, l.remove(num) for num in l]))
    # for subset problem can be modelized as take (1) or omit (0)
    # 2d matrix cache until index i and target
    s = 0
    for num in nums:
        s += num

    if s % 2 != 0:
        return False
    else:
        cache = [[0 for i in range(s // 2 + 1)] for j in range(len(nums))]
        cache[0][s // 2] = 1
        cache[0][s // 2 - nums[0]] = 1
        for i in range(1, len(cache)):
            for j in range(len(cache[0])):
                if j + nums[i] > s // 2:
                    cache[i][j] = cache[i - 1][j]
                else:
                    cache[i][j] = cache[i - 1][j] or cache[i - 1][j + nums[i]]
                if cache[i][0]:
                    return True

    return False