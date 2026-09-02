class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        curSum = 0

        for x in range(len(nums)):
            if curSum < 0:
                curSum = 0

            curSum += nums[x]
            res = max(curSum, res)

        return res

        