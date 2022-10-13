import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        al = { i: [] for i in range(n)} # 0 : [cost, node]
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                al[i].append([dist, j])
                al[j].append([dist, i])
        
        visit = set()
        res = 0
        minH = [[0, 0]] #[cost, node]
        heapq.heapify(minH)
        
        while len(visit) < n: #while minH: worked for all but 1 test case, got tle for 1. is this because the for loop or the this while?
            cost, cur = heapq.heappop(minH)
            if cur in visit:
                continue
            res += cost
            visit.add(cur)
            
            for c, ne in al[cur]:
                heapq.heappush(minH, [c, ne])
        
        return res