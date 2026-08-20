class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [0,1], [-1, 0], [0, -1]]
        queue = deque()
        visited = set()

        for x in range(len(board)):
            for y in range(len(board[0])):
                if ((x == 0 or x == len(board) - 1) or (y == 0 or y == len(board[0]) - 1)) and board[x][y] == 'O':
                    board[x][y] = 'T'
                    queue.append((x, y))
                    visited.add((x, y))

        while queue:
            row, col = queue.popleft()

            for r, c in directions:
                if row + r > 0 and row + r < len(board) and col + c > 0 and col + c < len(board[0]) and (row + r, col + c) not in visited and board[row + r][col + c] == 'O':
                    board[row + r][col + c] = 'T'
                    queue.append((row + r, col + c))
                    visited.add((row + r, col + c))

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'T':
                    board[x][y] = 'O'