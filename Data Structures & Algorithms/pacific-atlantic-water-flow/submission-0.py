class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0,1], [1,0], [-1,0], [0, -1]]
        atlSet = set()
        pacSet = set()
        res = []

        atlQueue = deque()
        pacQueue = deque()

        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if x == 0 or y == 0:
                    pacQueue.append((x, y))
                    pacSet.add((x, y))

        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if x == len(heights) - 1 or y == len(heights[0]) - 1:
                    atlQueue.append((x, y))
                    atlSet.add((x, y))

        while atlQueue:
            row, col = atlQueue.popleft()


            for dirX, dirY in directions:
                newX = row + dirX
                newY = col + dirY

                if newX >= 0 and newY >= 0 and newX < len(heights) and newY < len(heights[0]) and (newX, newY) not in atlSet and heights[newX][newY] >= heights[row][col]: 
                    atlSet.add((newX, newY))
                    atlQueue.append((newX, newY))


        while pacQueue:
            row, col = pacQueue.popleft()


            for dirX, dirY in directions:
                newX = row + dirX
                newY = col + dirY

                if newX >= 0 and newY >= 0 and newX < len(heights) and newY < len(heights[0]) and (newX, newY) not in pacSet and heights[newX][newY] >= heights[row][col]: 
                    pacSet.add((newX, newY))
                    pacQueue.append((newX, newY))


            

        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if (x, y) in pacSet and (x, y) in atlSet:
                    res.append([x, y])

        return res


        


             
