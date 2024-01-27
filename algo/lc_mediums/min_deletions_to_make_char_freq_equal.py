class Solution:
    def minDeletions(self, s: str) -> int:
        from collections import defaultdict 
        from heapq import heapify, heappop, heappush
        
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        
        freq = [-v for v in d.values()]
        delCount = 0
        heapify(freq)

        while freq:
            top = -1 * heappop(freq) 
            
            if freq and top == -1 * freq[0]:
                top -= 1
                delCount += 1

                if top:
                    heappush(freq, -top)
        
        return delCount
            


