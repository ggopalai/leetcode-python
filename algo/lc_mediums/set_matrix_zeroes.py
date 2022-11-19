# 1. Brute Force 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        zr = []
        zc = []
        for i in range(r):
            for j in range(c):
                if not matrix[i][j]:
                    zr.append(i)
                    zc.append(j)
        
        for i in zr:
            for j in range(c):
                matrix[i][j] = 0
        
        for i in zc:
            for j in range(r):
                matrix[j][i] = 0