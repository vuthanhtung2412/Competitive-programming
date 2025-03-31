def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    res = []
    counter = dict()
    for w in words:
        count = counter.get(w, 0)
        counter[w] = count + 1
    words_counter = counter.copy()
    length = len(words[0])
    s += " " * (length - 1)

    for i in range(length):
        l = i
        r= i
        while r < len(s):
            if s[r : r + length] in words_counter:
                if s[r : r + length] in counter:
                    counter[s[r : r + length]] -= 1
                    if counter[s[r : r + length]] == 0:
                        del counter[s[r : r + length]]
                    if not counter:
                        res.append(l)
                        counter[s[l : l + length]] = 1
                        l += length
                    r += length
                else:
                    count = counter.get(s[l : l + length], 0)
                    counter[s[l : l + length]] = count + 1
                    l += length
            else:
                l = r + length
                r += length
                counter = words_counter.copy()
    return res


# print(findSubstring("barfoothefoobarman", ["foo", "bar"]))  # [0,9]
# print(findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))  # [6,9,12]
# print(
#     findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
# )  # [8]

print(
    findSubstring(
        "lingmindraboofooowingdingbarrwingmonkeypoundcake",
        ["fooo", "barr", "wing", "ding", "wing"],
    )
)  # [13]
