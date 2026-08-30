class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStart = 0
        resLength = 0

        for x in range(len(s)):

            l, r = x, x

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLength:
                    resStart = l
                    resLength = r - l + 1

                l -= 1
                r += 1

            
            l, r = x, x + 1


            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLength:
                    resStart = l
                    resLength = r - l + 1
                l -= 1
                r += 1
        
        return s[resStart: resStart + resLength]


        

        

        




        