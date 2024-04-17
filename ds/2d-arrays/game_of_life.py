class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        rows, cols = len(board), len(board[0])
        

        dirs = [(-1, -1), (1, 1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(rows):
            for j in range(cols):
                count = 0
                for dr, dc in dirs:
                    r, c = i + dr, j + dc
                    if r in range(rows) and c in range(cols) and abs(board[r][c]) == 1:
                        count += 1
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 2
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

        return board

        

