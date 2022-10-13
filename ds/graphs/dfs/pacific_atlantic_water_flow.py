#1. Naive solution O(m  * n)^2
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #pacific - up or left
        #atlantic - down or right
        rows, cols = len(heights), len(heights[0])
        res = []
        stack = []

        def dfs(r, c):
            aFlag = False
            pFlag = False            
            seen = set()
           
            while stack:
                row, col = stack.pop()
                if (row, col) in seen:
                    continue
                seen.add((row, col))
                
                if row == 0 or col == 0:
                    pFlag = True
                if row == (rows - 1) or col == (cols - 1):
                    aFlag = True
                    
                directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
                for dr, dc in directions:
                    cr, cc = row + dr, col + dc
                    if cr in range(rows) and cc in range(cols) and heights[cr][cc] <= heights[row][col] and (cr, cc) not in seen:
                        stack.append((cr, cc))
            
            if aFlag and pFlag:
                res.append([r, c])
        
        for r in range(rows):
            for c in range(cols):
                stack.append((r, c))
                dfs(r, c)
        
        return res        
                
#2. Instead, we can start from the oceans and see which all cells can be reached. The final result will be an intersection of these 2.
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        res = []
        atl, pac = set(), set()
        
        def dfs(r, c, visit, prevHeight):
            if (r,c) in visit or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        #first and last rows
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        #first and last columns
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        #or
        # c = pac.intersection(atl)
        # for i, j in c:
        #     res.append([i, j])
        
        return res        
                
        