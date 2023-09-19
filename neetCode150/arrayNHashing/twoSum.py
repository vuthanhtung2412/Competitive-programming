def twoSumHash(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # hashing
    d = {}
    for i in range(len(nums)):
        if nums[i] in d:
            return [i, d.get(nums[i])]
        d[target - nums[i]] = i

def twoSum2pointer(nums, target):
    sNums = sorted(nums)
    s = 0
    b = 1
    somme = sNums[s] + sNums[b]
    while somme < target:
        if b == len(nums) - 1:
            break
        b += 1
        somme = sNums[s] + sNums[b]
    while somme != target:
        if somme < target:
            s += 1
        if somme > target:
            b -= 1
        somme = sNums[s] + sNums[b]

    sr = -1
    br = -1
    for i in range(len(sNums)):
        if sr != -1 and br != -1:
            break
        if sNums[s] == nums[i] and sr == -1:
            sr = i
        elif sNums[b] == nums[i] and br == -1:
            br = i

    return [sr, br]


print(twoSumHash([2, 7, 11, 15], 9))
print(twoSum2pointer([2, 7, 11, 15], 9))