class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        


        def dfs(c, memo):

            if c in memo:
                return memo[c]

            if c >= len(cost):
                return 0
            memo[c] = cost[c] + min(dfs(c + 1, memo), dfs(c + 2, memo))
            return memo[c]
        

        return min(dfs(0, {}), dfs(1, {}))