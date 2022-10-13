class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        
        minSum = [[0 for _ in range(c)] for _ in range(r)]

        for i in range(r):
            for j in range(c):
                #base-case
                if i == 0 and j == 0:
                    minSum[i][j] = grid[i][j]
                
                #first row or column
                elif i == 0 or j == 0:
                    minSum[i][j] = (grid[i][j] + minSum[0][j-1]) if i == 0 else (grid[i][j] + minSum[i-1][j])
                #recurrence
                else:
                    minSum[i][j] = grid[i][j] + min(minSum[i-1][j], minSum[i][j-1])
                
        return minSum[r-1][c-1]
        