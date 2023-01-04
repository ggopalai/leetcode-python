from collections import defaultdict
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = defaultdict(int)
        
        for i in tasks:
            d[i] += 1
        
        count = 0
        for i in d.values():
            if i == 1:
                return -1
            elif i % 3 == 0:
                count += i // 3
            else:
                count += (i // 3) + 1
        
        return count
       
        