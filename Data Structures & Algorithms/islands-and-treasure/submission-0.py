class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque()
        visited = set()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    queue.append((x, y))
                    visited.add((x, y))

        while queue:
            for x in range(len(queue)):
                row, col = queue.popleft()
                for dirx, diry in directions:
                    newX = row + dirx
                    newY = col + diry

                    if (newX, newY) not in visited and newX >= 0 and newY >= 0 and newX < len(grid) and newY < len(grid[0]) and grid[newX][newY] != -1:
                        queue.append((newX, newY))
                        visited.add((newX, newY))

                        grid[newX][newY] = grid[row][col] + 1

                  


        