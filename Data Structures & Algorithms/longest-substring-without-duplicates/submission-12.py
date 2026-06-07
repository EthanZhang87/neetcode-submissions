class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l,r = 0, 1
        if len(set(s)) == 1:
            return 1
        elif len(set(s)) == 2:
            return 2

        while r < len(s) - 1:
            if s[r + 1] not in s[l:r+1]:
                r += 1
                if len(s[l : r + 1]) > longest:
                    longest = len(s[l : r + 1])
            else:
                l += 1
        return longest

            
        
