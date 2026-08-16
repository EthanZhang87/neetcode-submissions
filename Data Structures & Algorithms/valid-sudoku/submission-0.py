class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for x in range(len(board))]
        cols = [[] for x in range(len(board[0]))]

        threeGrids = [[] for x in range((len(board) // 3) * (len(board[0]) // 3))]


        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] != '.':
                    row = x // 3
                    col = y // 3
                    if board[x][y] in rows[x] or board[x][y] in cols[y] or board[x][y] in threeGrids[row * 3 + col]:
                        return False
                    else:
                        rows[x].append(board[x][y])
                        cols[y].append(board[x][y])
                        threeGrids[row * 3 + col].append(board[x][y])

        


        return True        