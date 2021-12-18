"""
Runtime: 100 ms, faster than 95.65% of Python3 online submissions for Matrix Diagonal Sum.
Memory Usage: 14.5 MB, less than 48.44% of Python3 online submissions for Matrix Diagonal Sum.
"""
def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if i == j or i + j == len(mat)-1:
                    res += mat[i][j]
                    
        return res