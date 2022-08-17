class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        
        q = [(sr, sc)]
        seen = set()
        ogc = image[sr][sc]
        image[sr][sc] = color
        rows, cols = len(image), len(image[0])
        
        while q:
            r, c = q.pop(0)
            if (r, c) in seen:
                continue
                
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                if row in range(rows) and col in range(cols) and image[row][col] == ogc:
                    image[row][col] = color
                    q.append((row, col))
        
        return image
        
        