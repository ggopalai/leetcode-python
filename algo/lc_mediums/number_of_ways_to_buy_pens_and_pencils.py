class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        pens = total // cost1
        count = 0
        for i in range(pens + 1):
            remaining = total - (i * cost1)
            pencils = remaining // cost2
            count += pencils + 1
        
        return count







        