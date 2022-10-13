class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        
        #pre-process to find number of fresh and rotting oranges.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
    
        while q and fresh:
            # for inside the while ensures that all rotting oragnes get processed at the same time step. also the len(q) is a snapshot and doesn't 
            # change dynamically. 
            for i in range(len(q)):
                r, c = q.pop(0)
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    row, col = r + dr, c + dc
                    if row not in range(rows) or col not in range(cols) or grid[row][col] in [0,2]:
                        continue
                    q.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1