class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = nums[0]
        maxSum = nums[0]

        for x in range(1, len(nums)):
            curMax = max(nums[x], curMax + nums[x])
            maxSum = max(maxSum, curMax)

        return maxSum