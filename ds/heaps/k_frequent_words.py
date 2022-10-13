import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mh = []
        d = {}
        for i in words:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for z, v in d.items():
            mh.append([-v, z])
        
        heapq.heapify(mh)
        res = []
        while k > 0:
            a, b = heapq.heappop(mh)
            res.append(b)
            k -= 1
        
        return res