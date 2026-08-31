class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0

        def dfs(i, j):
            nonlocal res
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            count = 0

            for x, y in directions:
                newX = i + x
                newY = j + y
     
                

                if newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[0]) and grid[newX][newY] == 1:
                    count += 1
                    if (newX, newY) not in visited:
                        visited.add((newX, newY))
                        dfs(newX, newY)
    
                   

            res += (4 - count)
                


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and (x,y) not in visited:
                    visited.add((x, y))
                    dfs(x, y)

        return res