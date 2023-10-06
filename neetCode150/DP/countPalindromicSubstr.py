def countSubstrings(s: str) -> int:
    res = 0
    l = 0
    i = 0
    while i < len(s):
        tmp = i
        # detect middle point
        while i < len(s) and s[i] == s[l]:
            i += 1

        res += i - tmp + (i - tmp) * (i - tmp - 1) // 2

        tmp = i - 1

        while i < len(s) and l - 1 >= 0 and s[i] == s[l - 1]:
            l -= 1
            i += 1
            res += 1

        i = tmp + 1
        l = i

    return res