class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r, c = len(mat), len(mat[0])
        mv = 10001
        res = [[mv for _ in range(c)] for _ in range(r)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # first pass check left and top
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i-1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j-1] + 1)
        
        # second pass check bottom and right
        for i in range(r-1, -1, -1):
            for j in range(c-1, -1, -1):
                if i < r - 1:
                    res[i][j] = min(res[i][j], res[i+1][j] + 1)
                if j < c - 1:
                    res[i][j] = min(res[i][j], res[i][j+1] + 1)

        return res
        