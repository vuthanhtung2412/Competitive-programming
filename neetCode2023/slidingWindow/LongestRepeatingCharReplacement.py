def characterReplacement(s: str, k: int) -> int:
    # find the range that has the highest freq of occurence of 1 char
    # if we find another largest window we keep scanning with that size
    d = {}
    curr = 0
    res = 0
    l = 0
    for i in range(len(s)):

        # update most frequent element
        tmp = 1 + d.get(s[i], 0)
        d[s[i]] = tmp
        if tmp > curr:
            curr = tmp

        if i - l + 1 - curr > k:
            d[s[l]] = d.get(s[l], 0) - 1
            l += 1


        if res < i - l + 1:
            res = i - l + 1

    return res


print(characterReplacement("ABAA", 0))
