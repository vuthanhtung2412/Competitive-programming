# My solution
def myMinWindow(s: str, t: str) -> str:
    se = set()
    dt = {}
    for c in t:
        se.add(c)
        dt[c] = 1 + dt.get(c, 0)

    l = 0
    r = 100000
    res = ""
    ds = {}
    for i in range(len(s)):
        tmp = ds.get(s[i], 0) + 1
        if s[i] in se and tmp >= dt[s[i]]:
            se.remove(s[i])
        ds[s[i]] = tmp

        while not se:
            if i - l + 1 < r:
                res = s[l:i + 1]
                r = i - l + 1

            tmp = ds.get(s[l]) - 1
            if s[l] in dt and tmp < dt[s[l]]:
                se.add(s[l])
            ds[s[l]] = tmp

            l += 1

    return res

# solution on Neetcode
def NCMinWindow(s: str, t: str) -> str:
    # keep track of missing char with only an int instead of a set
    # not better by too much compare to my solutiuon
    dt = {}
    rest = 0
    for c in t:
        if c not in dt:
            dt[c] = 1
            rest += 1
        else:
            dt[c] += 1

    l = 0
    r = 100000
    res = ""
    ds = {}
    for i in range(len(s)):
        tmp = ds.get(s[i], 0) + 1
        if s[i] in dt and tmp == dt[s[i]]:
            rest -= 1
        ds[s[i]] = tmp

        while rest == 0:
            if i - l + 1 < r:
                res = s[l:i + 1]
                r = i - l + 1

            tmp = ds.get(s[l]) - 1
            if s[l] in dt and tmp < dt[s[l]]:
                rest += 1
            ds[s[l]] = tmp

            l += 1

    return res

print(NCMinWindow("ADOBECODEBANC", "ABC"))