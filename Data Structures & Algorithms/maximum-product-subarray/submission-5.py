class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        currMin, currMax = 1, 1
        for x in nums:
            if x == 0:
                currMin = 1
                currMax = 1
                continue
            temp = currMax * x
            currMax = max(currMax * x, currMin * x, x)
            currMin = min(temp, currMin * x, x)

            res = max(res, currMax)

        return res

        