class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        real = set(nums)
        res = 0

        for x in real:
            if x - 1 in real:
                continue 
            length = 1

            while x + 1 in real:
                length += 1
                x += 1

            res = max(res, length)

        return res