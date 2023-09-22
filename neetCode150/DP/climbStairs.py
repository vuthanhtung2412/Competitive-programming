def climbStairs(n: int) -> int:
    # climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
    if n == 1:
        return 1
    a = 1
    b = 2
    for i in range(2, n):
        flag = a + b
        a = b
        b = flag

    return b
