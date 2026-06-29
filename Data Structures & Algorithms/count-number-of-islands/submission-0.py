class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, col = len(grid), len(grid[0])
        res = 0
        directions = [[-1,0], [0,-1],[1, 0], [0,1]]

        def dfs(grid, r, c):
            if r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] == '0':
                return           

            
            grid[r][c] = '0'

            for dx, dy in directions:
                dfs(grid, r + dx, c + dy)

        for x in range(rows):
            for y in range(col):
                if grid[x][y] == '1':
                    dfs(grid, x, y)
                    res += 1


        return res