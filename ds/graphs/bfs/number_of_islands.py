import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        #breadth-first-search to cover all the adjacent 1s
        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r,c))
            
            while q:
                r, c = q.popleft()
                #down, up, right and left cells
                directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if (r + dr) in range(rows) and (c + dc) in range(cols) and grid[r + dr][c + dc] == "1" and ((r + dr), (c + dc)) not in visit:
                        q.append((r + dr, c + dc))
                        visit.add((r + dr, c + dc))
        
        #for each new island, call bfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
                    
        
        