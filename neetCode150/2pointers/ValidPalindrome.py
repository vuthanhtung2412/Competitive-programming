def isPalindrome(s: str) -> bool:
    filtered_s = ''.join(filter(str.isalnum, s)).lower()
    l = 0
    r = len(filtered_s) - 1
    while l < r:
        if filtered_s[l] == filtered_s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True