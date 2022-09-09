class Solution(object):
    def romanToInt(self, s):
        result = 0
        skipNot = True
        for i in range(len(s)):
            if skipNot:         
                if s[i] == "I":
                    if i != len(s)-1:
                        if s[i+1]=="V":
                            result += 4
                            skipNot = False
                            continue
                        elif s[i+1]=="X":
                            result += 9
                            skipNot = False
                            continue
                    result += 1
                elif s[i] == "V":
                    result += 5
                elif s[i] == "X":
                    if i != len(s)-1:
                        if s[i+1]=="L":
                            result += 40
                            skipNot = False
                            continue
                        elif s[i+1]=="C":
                            result += 90
                            skipNot = False
                            continue
                    result += 10
                elif s[i] == "L":
                    result += 50
                elif s[i] == "C":
                    if i != len(s)-1:
                        if s[i+1]=="D":
                            result += 400
                            skipNot = False
                            continue
                        elif s[i+1]=="M":
                            result += 900
                            skipNot = False
                            continue
                    result += 100
                elif s[i] == "D":
                    result += 500
                elif s[i] == "M":
                    result += 1000
            else:
                skipNot = True
        return result
            