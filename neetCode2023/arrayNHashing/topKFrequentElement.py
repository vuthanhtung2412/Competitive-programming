def topKFrequentSort(nums, k):
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


def topKFrequentHash(nums, k):
    count = {}
    freq = [list() for _ in range(len(nums))]
    # Use frequency as a representation

    for i in nums:
        count[i] = 1 + count.get(i, 0)

    for ke, v in count.items():
        freq[v-1].append(ke)

    res = []
    for i in range(len(nums) - 1, -1, -1):
        res += freq[i]
        if len(res) == k:
            return res

    return res


# print(topKFrequentSort([1, 1, 1, 2, 2, 3], 2))
print(topKFrequentHash([1, 1, 1, 2, 2, 3], 2))
