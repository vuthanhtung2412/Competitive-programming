def groupAnagrams_sort(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # word sorting method
    d = {}
    for w in strs:
        sw = ''.join(sorted(w))
        # d[sw] = d.get(sw, []).append(w) # append always return none

        # solution use concatenation instead of append, however concatenation time complexity is O(n)
        # d[sw] = d.get(sw, []) + [w]

        # fastest way
        if sw in d:
            d[sw].append(w)
        else:
            d[sw] = [w]
    return list(d.values())

# deep copy and shallow copy in Python
def groupAnagrams_hash(strs):
    # use set as key and char to hex
    # use set as key and char to hex
    l = [0] * 26  # there are 26 letters
    d = {}
    for w in strs:
        for c in w:
            l[ord(c) - ord('a')] += 1
        s = tuple(l)
        if s in d:
            d[s].append(w)
        else:
            d[s] = [w]
        l = [0] * 26
    return list(d.values())


print(groupAnagrams_sort(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams_hash(["eat","tea","tan","ate","nat","bat"]))