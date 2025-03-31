def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    l = 0
    r = len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid - 1] < target and target <= nums[mid]:
            return mid
        elif target <= nums[mid]:
            r = mid
        else:
            l = mid + 1
    return l
