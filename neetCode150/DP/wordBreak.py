from functools import reduce
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    # wordBreak(s) = reduce(or, [wordBreak(s[:-len(w)]) for w in wordDict])
    # bottom up approach
    res = [False for _ in range(len(s) + 1)]
    res[0] = True
    for i in range(1, len(s)+1):
        for w in wordDict:
            if i - len(w) >= 0 and res[i-len(w)] and s[i - len(w):i] == w:
                res[i] = True
                break

    return res[-1]


print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("applepenapple", ["apple", "pen"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
