class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        count = 0
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    count += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))


        if count == 0:
            return 0
            
        mins = 0
        while queue:
            mins += 1
            for y in range(len(queue)):
                r, c = queue.popleft()
                
                for x in directions:
                    dirx, diry = r + x[0], c + x[1]

                    if 0 <= dirx < len(grid) and 0 <= diry < len(grid[0]) and grid[dirx][diry] == 1:
                        count -= 1
                        grid[dirx][diry] = 2
                        queue.append((dirx, diry))


        if count > 0:
            return -1
        else:
            return mins - 1






        
        