import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        mh = []
        heapq.heapify(mh)
        
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(mh, matrix[i][j])
        
        res = 0
        
        while k:
            res = heapq.heappop(mh)
            k -= 1
        
        return res
            
            
            