def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    s = set()
    curr = n
    while curr not in s:
        s.add(curr)
        new = 0
        tmp = curr
        while tmp != 0:
            new += (tmp % 10) ** 2
            tmp = tmp // 10
        if new == 1:
            return True
        curr = new

    return False


print(isHappy(19))
print(isHappy(2))
