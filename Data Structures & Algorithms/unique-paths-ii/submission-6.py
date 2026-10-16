class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid) -1][len(obstacleGrid[0]) - 1] == 1:
            return 0

        def dfs(r, c, memo):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == len(obstacleGrid) - 1 and c == len(obstacleGrid[0]) - 1:
                return 1

            if r == len(obstacleGrid) or c == len(obstacleGrid[0]) or r < 0 or c < 0:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            memo[(r, c)] = dfs(r, c + 1, memo) + dfs(r + 1, c, memo)

            return memo[(r, c)]


        return dfs(0, 0, {})
           
            

            

        