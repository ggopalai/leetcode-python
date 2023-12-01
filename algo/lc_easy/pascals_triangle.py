class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 1 and 2 are base cases
        pt = [[1]]
        if numRows == 1:
            return pt
        pt.append([1, 1])
        
        if numRows == 2:    
            return pt

        for i in range(2, numRows):
            
            # every row starts and ends with a 1
            start = [1]
            
            # number of additions
            for j in range(i - 1):
                start.append(pt[i - 1][j] + pt[i - 1][j + 1])
            
            start.append(1)
            pt.append(start)
        
        return pt

        