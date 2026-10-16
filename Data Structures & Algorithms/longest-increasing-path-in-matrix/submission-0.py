class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            res = 1
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for x, y in directions:
                newX = r + x
                newY = c + y

                if (0 <= newX < len(matrix) and
                    0 <= newY < len(matrix[0]) and
                    matrix[newX][newY] > matrix[r][c]):

                    res = max(res, 1 + dfs(newX, newY))

            memo[(r, c)] = res
            return res

        res = 0

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                res = max(res, dfs(x, y))

        return res