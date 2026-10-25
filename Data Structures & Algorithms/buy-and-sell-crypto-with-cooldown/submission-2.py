class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i, canBuy, memo):
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            if i >= len(prices):
                return 0

            if canBuy:
                memo[(i, canBuy)] = max(dfs(i + 1, False, memo) - prices[i], dfs(i + 1, canBuy, memo))
            else:
                memo[(i, canBuy)] = max(prices[i] + dfs(i + 2, True, memo), dfs(i + 1, canBuy, memo))
            return memo[(i, canBuy)]

        return dfs(0, True, {})