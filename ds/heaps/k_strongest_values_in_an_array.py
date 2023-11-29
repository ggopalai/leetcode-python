import heapq
from collections import defaultdict
d = defaultdict(int)
class Solution:
    """
    Time - O (n log n)
    Space - O(n)
    """
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # n log n
        arr.sort()
        m = arr[(len(arr) - 1) // 2]

        # n
        strengths = [0] * len(arr)
        for i, val in enumerate(arr):
            strengths[i] = (abs(val - m), val)
        
        # max heap
        # adding two values takes care of the tie breaker case.
        heap = []
        for s, val in strengths: 
            heapq.heappush(heap, (-s, -val)) # log n * n times
        
        res = []
        while k:
            _, val = heapq.heappop(heap) # O(1)
            res.append(-val)
            k -= 1
        
        return res

        

        


        