class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        count2 = 0
        def dfs(r, c, ):
            nonlocal count2
            directions = [[1, 0], [0,1], [-1, 0], [0,-1]]

            grid[r][c] = 0
            count2 += 1

            
            for x in directions:
                dirx, diry = r + x[0], c + x[1]
                if 0 <= dirx < len(grid) and 0 <= diry < len(grid[0]) and grid[dirx][diry] == 1:
                    dfs(dirx, diry)
                    
            
         

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count2 = 0
                    dfs(r, c)
                    count = max(count, count2)
             

        return count



        

        