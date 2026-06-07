class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxVal = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                maxVal = max(maxVal, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return maxVal

            




        