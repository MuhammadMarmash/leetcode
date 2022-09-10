class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        while i < len(t):
            if t[i] not in s:
                t = t.replace(t[i], "")
                continue
            i += 1

        return (s in t)