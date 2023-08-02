def twoSum(nums, target):
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

print(twoSum([2, 7, 11, 15], 9))