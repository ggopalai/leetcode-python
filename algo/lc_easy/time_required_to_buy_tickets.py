# 1. brute-force : timed out. 
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        
        while tickets[k]:
            i = 0
            while i < len(tickets) and tickets[i]:
                tickets[i] -= 1
                time += 1
                i += 1
        
        return time

#Worked
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        n = len(tickets)
        q = []
        result = [0 for i in range(n)]
        
        for i in range(n):
            q.append(i)
        
        while q:
            i = q.pop(0)
            tickets[i] -= 1
            time += 1
            
            if tickets[i] > 0:
                q.append(i)
            
            if tickets[i] == 0:
                result[i] = time
        
        return result[k]
            
            