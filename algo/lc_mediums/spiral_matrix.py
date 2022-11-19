class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        # setting right and bottom 1 step ahead. (as range excludes second arguement)
        # left and top
        l, t = 0, 0
        # right and bottom
        r, b = len(matrix[0]), len(matrix)
        
        while l < r and t < b:
            
            # top left to right 
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            
            #right top to bottom
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1
            
            # row or column vector column case
            if not (t < b and l < r):
                break
            
            # bottom right to left 
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            
            # left bottom to top 
            for i in range(b - 1,  t - 1, -1):
                res.append(matrix[i][l])
            l += 1
        
        return res
            
            