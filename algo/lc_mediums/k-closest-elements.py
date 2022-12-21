import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        mh = []
        res = []

        for i in arr:
            diff = abs(i - x)
            heapq.heappush(mh, (diff, i))
        
        while k:
            diff, num = heapq.heappop(mh)
            res.append(num)
            k -= 1
        
        return sorted(res)

