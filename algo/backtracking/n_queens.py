class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pDiag = set()
        nDiag = set()
        
        board = [["." for i in range(n)] for row in range(n)] # or board = [["."] * n for i in range(n)]
        res = []
        
        def backtrack(r):
            #when when we reach the row next to last, we know we've reached the result. 
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            #for each column in row r
            for c in range(n):    
                if c in cols or (r+c) in pDiag or (r-c) in nDiag:
                    continue
                
                cols.add(c)
                pDiag.add(r + c)
                nDiag.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)
                
                cols.remove(c)
                pDiag.remove(r + c)
                nDiag.remove(r - c)
                board[r][c] = "."
        
        #start with row 0 
        backtrack(0)
        
        return res