class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]

        currMax, currMin = 0, 0

        total = 0

        for n in nums:
            currMax = max(n, currMax + n)
            currMin = min(currMin + n, n) 

            total += n

            globalMax = max(globalMax, currMax)

            globalMin = min(globalMin, currMin)

        if globalMax < 0:
            return globalMax
        else:
            return max(globalMax, total - globalMin)

        
