def longestPalindrome(s: str) -> str:
    # longestPalindrome(s) = longestPalindrome(s[-1]), currPalin
    # This thing is more of a 2 pointer problem than a dynamic programming
    if s:
        l = 0
        res = s[0]
        i = 0
        while i < len(s):
            tmp = i
            # detect middle point
            while i < len(s) and s[i] == s[l]:
                i += 1

            while i < len(s) and l - 1 >= 0 and s[i] == s[l - 1]:
                l -= 1
                i += 1

            if i - l > len(res):
                res = s[l: i]
                print(res)

            i = tmp + 1
            l = i

        return res

    else:
        return ""


# PREVIOUS WRONG SOLUTION AND THEIR PROBLEMS
def longestPalindrome1(s: str) -> str:
    # longestPalindrome(s) = longestPalindrome(s[-1]), currPalin
    # This thing is more of a 2 pointer problem than a dynamic programming
    # PROBLEM: Consume mid-point if that mid-point is in a previous palindrome
    if s:
        l = 0
        res = s[0]
        i = 0
        while i < len(s):
            # detect middle point
            while i < len(s) and s[i] == s[l]:
                i += 1

            while i < len(s) and l - 1 >= 0 and s[i] == s[l - 1]:
                l -= 1
                i += 1

            if i - l > len(res):
                res = s[l: i]
                print(res)

            l = i

        return res
    else:
        return ""


def longestPalindrome2(s: str) -> str:
    # PROBLEM: only check the case of 1 and 2 mid-char -> have to check n-chars case
    if s:
        l = 0
        r = 0
        res = s[0]
        for i in range(1, len(s)):
            # Initialization of palidromic count
            if l == r:
                if s[i] == s[l]:  # even case
                    r += 1
                elif l - 1 >= 0 and s[l - 1] == s[i]:  # odd case
                    l -= 1
                    r += 1
                else:
                    l = i
                    r = i
            else:
                if r + l - i >= 0 and s[i] == s[r + l - i]:
                    r += 1
                    l -= 1
                else:
                    r = i
                    l = i

            if r - l + 1 > len(res):
                res = s[l: (r + 1)]

        return res
    else:
        return ""
