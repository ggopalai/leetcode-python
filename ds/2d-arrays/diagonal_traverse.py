class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        from collections import defaultdict
        d = defaultdict(list)
        res = []
        r, c = len(mat), len(mat[0])

        for i in range(r):
            for j in range(c):
                d[i+j].append(mat[i][j])
        
        for k, v in d.items():
            if k % 2 == 0:
                res.extend(reversed(v))
            else:
                res.extend(v) 
        
        return res


        