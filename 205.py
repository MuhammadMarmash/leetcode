class Solution(object):
    def isIsomorphic(self, s, t):
        mapping = {}
        for i in range(len(s)):
            if (s[i] not in mapping.keys()) and (t[i] not in mapping.values()):
                mapping[s[i]] = t[i]
        for y in range(len(s)):
            if (s[y] == t[y]) and (s[y] not in mapping.keys() or t[y] not in mapping.values()):
                return False
            if s[y] in mapping.keys():
                s = s[:y] + mapping[s[y]] + s[y + 1 :]
        if s == t:
            return True
        return False