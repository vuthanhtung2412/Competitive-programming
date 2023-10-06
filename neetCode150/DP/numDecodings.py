def numDecodings(s: str) -> int:
    # same principle as wordbreak
    # numDecodings(s) = reduce(+, [numDecodings(s[:-len(c)]) if c == s[-len(c)] else 0 for c in codes])
    # bottom up approach
    if len(s) == 1:
        return int(1 <= int(s[0]) <= 26)
    else:
        if 1 <= int(s[0]) <= 26:
            a = 1
        else:
            return 0

        b = 0
        if 1 <= int(s[1]) <= 26:
            b += 1

        if 10 <= int(s[:2]) <= 26:
            b += 1

        if b == 0:
            return 0

        for i in range(2, len(s)):
            tmp = b
            b = 0
            if 1 <= int(s[i]) <= 26:
                b += tmp

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                b += a

            if b == 0:
                return 0

            a = tmp

        return b
