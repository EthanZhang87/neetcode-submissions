class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0

        while r < len(s):
            if s[r] not in s[l:r]:
                res = max(res, r - l + 1)
                r += 1
            else:
                l += 1

        return res