class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        if len(nums) == 0:
            return 0

        real = set(nums)

        nums = list(real)

        
        res = 0

        for x in nums:
            length = 1
            while True:
                if x + 1 in nums:
                    length += 1
                    x = x + 1
                else:
                    break

            if length > res:
                res = length

        return res
                
            


        