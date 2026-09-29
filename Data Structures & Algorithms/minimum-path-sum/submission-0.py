class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c, memo):
            if (r, c) in memo:
                return memo[(r, c)]
            if r >= len(grid) or c >= len(grid[0]):
                return float("inf")

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[r][c]
            memo[(r, c)] = grid[r][c] + min(
                dfs(r + 1, c, memo),
                dfs(r, c + 1, memo)
            )
            return memo[(r, c)]
        return dfs(0, 0, {})