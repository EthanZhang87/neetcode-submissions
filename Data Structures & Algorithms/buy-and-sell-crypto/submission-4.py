class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSum = 0
        l, r = 0, 1
        while r <= len(prices) - 1:

            if prices[l] > prices[r]:
                l += 1
            else:
                if prices[r] - prices[l] > maxSum:
                    maxSum = prices[r]-prices[l]
                r += 1
            """
            if prices[l] > prices [r]:
                l += 1
                r += 1
            else:
                if prices[r] - prices[l] > maxSum:
                    maxSum = prices[r] - prices[l]
                r += 1"""
        return maxSum