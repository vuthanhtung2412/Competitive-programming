from typing import List
def threeSum(nums: List[int]) -> List[List[int]]:
    # scan the whole array, 2 sum for each number scanned
    # No need to keep the index
    nums = sorted(nums)
    res = []
    i = 0
    while i < len(nums) - 2:

        if nums[i] > 0:
            return res

        s = i + 1
        b = i + 2

        somme = nums[s] + nums[b]

        # It get too big
        if somme > -nums[i]:
            break
        # move the big pointer to the biggest
        while somme < -nums[i]:
            if b == len(nums) - 1:
                break  # only break the inner most loop
            b += 1
            somme = nums[s] + nums[b]

        while s < b:
            if somme == -nums[i]:
                res.append([nums[i], nums[s], nums[b]])
                b -= 1
                s += 1
                if s >= b:
                    break
                while nums[s] == nums[s - 1] and s < b:
                    s += 1
            elif somme < -nums[i]:
                s += 1
            elif somme > -nums[i]:
                b -= 1
            somme = nums[s] + nums[b]

        i += 1

        # skip duplicate
        while nums[i] == nums[i - 1] and i < len(nums) - 2:
            i += 1

    return res

print(threeSum([-2,-2,-2,0,1,2,2,2]))