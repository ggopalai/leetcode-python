import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        heap = []
        for c, v in d.items():
            heap.append([-1 * v, c])
        
        heapq.heapify(heap)
        res = []
        while k > 0:
            a, n = heapq.heappop(heap)
            res.append(n)
            k -= 1
        
        return res