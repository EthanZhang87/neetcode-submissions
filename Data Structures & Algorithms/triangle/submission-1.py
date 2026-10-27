class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        def dfs(row, col, memo):
            if (row, col) in memo:
                return memo[(row, col)]

            if row == len(triangle) - 1:
                return triangle[row][col]

            left = dfs(row + 1, col, memo)
            right = dfs(row + 1, col + 1, memo)

            memo[(row, col)] = triangle[row][col] + min(left, right)

            return memo[(row, col)]

            

        return dfs(0, 0, {})
            

        