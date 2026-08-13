class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numOfRows = len(matrix)
        numOfCols = len(matrix[0])

        l, r = 0, numOfRows * numOfCols - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // numOfCols
            col = mid % numOfCols

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1



        return False




