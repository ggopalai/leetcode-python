class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        
        # keep track of row, column, and box
        rm = defaultdict(list)
        cm = defaultdict(list)
        bm = defaultdict(list)

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                
                # box index - tuple of (row // 3, column // 3)
                bmi = ((i // 3), (j // 3))
                if cur != '.':
                    if cur in rm[i] or cur in cm[j] or cur in bm[bmi]:
                        return False
                    else:
                        rm[i].append(cur)
                        cm[j].append(cur)
                        bm[bmi].append(cur)

        return True        