class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        longest = 0
        l = 0

        for right in range(len(s)):
            while s[right] in char:
                char.remove(s[l])
                l += 1
            
            char.add(s[right])

            longest = max(longest, right-l+1)

        return longest
        

            
        
