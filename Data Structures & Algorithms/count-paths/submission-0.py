class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0

        def dfs(r, c, memo):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == (m - 1) and c == (n - 1):
                return 1

            if r >= m or c >= n:
                return 0
            memo[(r, c)] = dfs(r + 1, c, memo) + dfs(r, c + 1, memo)
            return memo[(r, c)]

        
        return dfs(0, 0, {})
            

        