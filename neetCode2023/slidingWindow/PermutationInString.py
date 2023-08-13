def checkInclusion(s1: str, s2: str) -> bool:
    d = {}
    l1 = len(s1)
    l2 = len(s2)
    if l1 > l2:
        return False

    for i in range(l1):
        d[s1[i]] = 1 + d.get(s1[i], 0)
    flag = 0

    for i in range(l1):
        d[s2[i]] = d.get(s2[i], 0) - 1
        if d[s2[i]] == 0:
            del d[s2[i]]
    if not d:
        return True

    for i in range(l1, l2):

        d[s2[i]] = d.get(s2[i], 0) - 1
        if d[s2[i]] == 0:
            del d[s2[i]]

        d[s2[i - l1]] = d.get(s2[i - l1], 0) + 1
        if d[s2[i - l1]] == 0:
            del d[s2[i - l1]]

        if not d:
            return True

    return False
