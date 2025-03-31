def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict = {}
    for num in nums:
        count = dict.get(num, 0)
        dict[num] = count + 1
    res = 0
    max_count = 0
    for k, v in dict.items():
        if v > max_count:
            res = k
            max_count = v
    return res
