class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        longest = 0
        left = 0
        for x in range(len(s)):
            dic[s[x]] = 1 + dic.get(s[x], 0)

            if (x -left + 1) - max(dic.values()) > k:
                dic[s[left]] -= 1
                left += 1

            longest = max(longest, x-left + 1)
        return longest
            

                

            
