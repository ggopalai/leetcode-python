# tle'd for 1 tc. how can i optimize this further? optimzation is similar to rotten oranges problem, check it out!
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        gate_indices = []
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    gate_indices.append((r, c))
        
        def bfs(i, j):
            """
            Use this function to update the minimum distance from gates to empty rooms.
            """
            seen = set()
            q = [(i, j, 0)]

            while q:
                row, col, dist = q.pop(0)

                seen.add ((row, col))
                
                # update min distane
                rooms[row][col] = min(dist, rooms[row][col])
                
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr in range(rows) and nc in range(cols) and rooms[nr][nc] != -1 and (nr, nc) not in seen and rooms[nr][nc] > dist + 1:
                        # explore new cell 
                        q.append((nr, nc, dist + 1))
                    
        for r, c in gate_indices:
            bfs(r, c)
        
        


        