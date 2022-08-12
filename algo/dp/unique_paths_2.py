class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        grid = [[0 for _ in range(c)] for _ in range(r)]
        
        #if there is an obstacle in the way, that block and all grids after become inaccessible along the first column.
        blocked = False
        for i in range(r):
            if obstacleGrid[i][0] == 1:
                blocked = True
            grid[i][0] = 1 if not blocked else 0
        
        #if there is an obstacle in the way, that block and all grids after become inaccessible along the first row.
        blocked = False
        for i in range(c):
            if obstacleGrid[0][i] == 1:
                blocked = True
            grid[0][i] = 1 if not blocked else 0
        
        #same recurrence as unique_paths but slight modification with obstacle block set to 0. 
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
                    
        return grid[r-1][c-1]
                    