class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        x = 0
        while x < len(s):
            if s[x] == 'I':
                if x < len(s) - 1 and s[x + 1] == "V":
                    res += 4
                    x += 2
                elif x < len(s) - 1  and s[x + 1] == 'X':
                    res += 9
                    x += 2
                else:
                    res += 1
                    x += 1

            elif s[x] == 'X':
                if x < len(s) - 1  and s[x + 1] == 'L':
                    res += 40
                    x += 2

                elif x < len(s) - 1  and s[x + 1] == 'C':
                    res += 90
                    x += 2

                else:
                    res += 10
                    x += 1

            elif s[x] == 'C':
                if x < len(s) - 1  and s[x + 1] == 'D':
                    res += 400
                    x += 2

                elif x < len(s) - 1  and s[x + 1] == 'M':
                    res += 900
                    x += 2
                else:
                    res += 100
                    x += 1

            else:
                res += roman[s[x]]
                x += 1
      
        return res

        
