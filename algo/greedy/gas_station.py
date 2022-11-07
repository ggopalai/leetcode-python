# 1. Naive - quadratic

# 2. Greedy - linear 
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #solution wouldn't exist in this case 
        if sum(cost) > sum(gas):
            return -1 
        
        total = 0
        start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            
            if total < 0:
                total = 0
                start = i + 1
        
        return start
            