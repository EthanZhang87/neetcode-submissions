class Solution:
    def tribonacci(self, n: int) -> int:

        def dfs(curr, memo): 
            if curr in memo:
                return memo[curr]
            if curr == 0:
                return 0

            if curr == 1 or curr == 2:
                return 1

            memo[curr] = dfs(curr - 1, memo) + dfs(curr - 2,  memo) + dfs(curr - 3, memo)

            return memo[curr]

        return dfs(n, {})
            
        