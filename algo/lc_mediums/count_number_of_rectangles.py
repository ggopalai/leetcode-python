class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        from collections import defaultdict
        import bisect

        res = []
        hm = defaultdict(list)
        
        for l, h in rectangles:
            hm[h].append(l)

        for _, v in hm.items():
            v.sort()
        
        for x, y in points:
            ans = 0
            for c in range(y, 101):
                if hm[c]:
                    ans += len(hm[c]) - bisect.bisect_left(hm[c], x)
            res.append(ans)

        return res