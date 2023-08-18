def lengthOfLongestSubstring(s: str) -> int:
    # 2 pointer
    # try shorten AMAP as soon as we find the first duplicates
    res = 0
    curr = set()
    l = 0
    for i in range(len(s)):
        if s[i] not in curr:
            curr.add(s[i])
            if res < i - l + 1:
                res = i - l + 1
        else:
            while s[l] != s[i] and l < i:
                curr.remove(s[l])
                l += 1
            l += 1
            curr.add(s[i])

    return res
