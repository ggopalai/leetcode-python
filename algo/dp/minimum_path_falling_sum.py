class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        ms = 0
        
        grid = [[0 for _ in range(r)] for _ in range(c)]
        
        for i in range(r):
            for j in range(c):
                #first row
                if i == 0:
                    grid[i][j] = matrix[i][j]
                #first and last column
                elif j == 0 or j == c-1:
                    grid[i][j] = matrix[i][j] + min(grid[i-1][j], grid[i-1][j+1]) if j == 0 else matrix[i][j] + min(grid[i-1][j], grid[i-1][j-1])
                #all other blocks
                else:
                    grid[i][j] = matrix[i][j] + min(grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1])
                
        return min(grid[r-1])       