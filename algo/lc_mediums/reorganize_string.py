class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter 
        from heapq import heapify, heappush, heappop
        c = Counter(s)
        mh = [(-v, k) for k, v in c.items()]
        heapify(mh)
        ans = ""

        while len(mh) > 1:
            f1, c1 = heappop(mh)
            f2, c2 = heappop(mh)

            ans += c1 + c2
            
            f1 += 1
            if f1 != 0:
                heappush(mh, (f1, c1))
            f2 += 1
            if f2 != 0:
                heappush(mh, (f2, c2))
        
        if not mh:
            return ans
            
        if mh[0][0] * -1 > 1:
            return ""
        
        return ans + mh[0][1]



