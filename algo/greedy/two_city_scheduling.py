# dp solution - quadratic 

# n log n
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs = []
        # c2 - c1 quantifies by how much b is more expensive than a.
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        diffs.sort()
        res = 0
        for i in range(len(costs)):
            if i < len(costs) // 2:
                res += diffs[i][2]
            else:
                res += diffs[i][1]
        
        return res
        
        
        