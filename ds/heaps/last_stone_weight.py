class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-i for i in stones]
        
        heapq.heapify(s)
        
        while len(s) > 1:
            a = -1 * heapq.heappop(s)
            b = -1 * heapq.heappop(s)
            r = a - b if a > b else b - a
            heapq.heappush(s, -1 * r)
        
        return -1 * s[0]