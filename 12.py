class Solution(object):
    def intToRoman(self, num):
        result = ""
        mapping = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]
        end = False
        while not end:
            end = True
            for x in mapping[::-1]:
                num -= x[1]
                if num >= 0:
                    result += x[0]
                    end = False
                    break
                num += x[1]

        return result

m = Solution()
print(m.intToRoman(3))
