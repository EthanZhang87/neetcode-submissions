class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        initial = image[sr][sc]
        image[sr][sc] = color


        queue = deque([[sr, sc]])


        directions = [[1, 0], [0,1], [-1, 0], [0, -1]]

        while queue:
            ele = queue.popleft()

            for x, y in directions:
                newX = ele[0] + x
                newY = ele[1] + y
                if newX >= 0 and newX < len(image) and newY >= 0 and newY < len(image[0]) and image[newX][newY] == initial:
                    image[newX][newY] = color
                    queue.append([newX, newY])
            

        return image
        