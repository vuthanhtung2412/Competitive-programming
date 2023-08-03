def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d = {}
    for x in nums:
        d[x] = 1 + d.get(x, 0)
    l = [(k, v) for k, v in d.items()]
    l.sort(key=lambda x: x[1], reverse=True)
    return [l[i][0] for i in range(k)]

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
