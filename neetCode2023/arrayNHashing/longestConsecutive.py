from typing import List
def longestConsecutive(nums: List[int]) -> int:
    res = 0
    s = set(nums)

    for n in nums:
        count = 0
        if n in s:
            count += 1
            s.remove(n)
            l = n - 1
            r = n + 1
            while l in s:
                count += 1
                s.remove(l)
                l -= 1

            while r in s:
                count += 1
                s.remove(r)
                r += 1

            if count > res:
                res = count
    return res