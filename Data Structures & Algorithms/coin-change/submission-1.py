class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dfs(i, memo):
            if i in memo:
                return memo[i]
            res = float('inf')
            if i < 0:
                return float('inf')

            if i == 0:
                return 0

            for x in range(len(coins)):
                res = min(res, 1 + dfs(i - coins[x], memo))
                
            memo[i] = res
            return memo[i]
        res = dfs(amount, {})
        if res == float('inf'):
            return -1

        return res
                
        