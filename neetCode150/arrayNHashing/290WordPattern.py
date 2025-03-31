def wordPattern(self, pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    m_char = {}
    m_word = {}
    words = s.split()
    if len(pattern) != len(words):
        return False
    for i in range(len(pattern)):
        if pattern[i] in m_char:
            if m_char[pattern[i]] != words[i] or m_word[words[i]] != pattern[i]:
                return False
        else :
            m_char[pattern[i]] = words[i]
            if words[i] in m_word and pattern[i] != m_word[words[i]]:
                return False
            m_word[words[i]] = pattern[i]
                
    return True
