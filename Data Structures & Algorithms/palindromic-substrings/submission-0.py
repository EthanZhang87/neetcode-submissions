class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for x in range(len(s)):
            l, r = x, x

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

            
            l, r = x, x + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res

            
        