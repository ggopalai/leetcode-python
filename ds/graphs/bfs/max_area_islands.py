class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        
        def bfs(r, c):
            curArea = 0
            seen.add((r,c))
            q = collections.deque()
            q.append((r, c))
            
            while q:
                curArea += 1
                row, col = q.popleft()
                
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    a, b = row + dr, col + dc
                    if a in range(rows) and b in range(cols) and grid[a][b] == 1 and (a, b) not in seen:
                        q.append((a, b))
                        seen.add((a, b))
            
            nonlocal maxArea
            maxArea = max(maxArea, curArea)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    bfs(r, c)
        
        return maxArea