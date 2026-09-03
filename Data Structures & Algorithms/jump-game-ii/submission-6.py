class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0

        l, r = 0, 0

        while r < len(nums) - 1:
            farthest = 0

            for x in range(l, r + 1):
                farthest = max(farthest, r + nums[x])

            l = r + 1
            r = farthest
            res += 1

        return res
       

        