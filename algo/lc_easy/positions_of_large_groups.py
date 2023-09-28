class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        st = s
        s, e = 0, 0
        for i in range(1, len(st)):
            if st[i-1] == st[i]:
                e = i
            else:
                if (e - s + 1) >= 3:
                    res.append([s, e])
                s, e = i, i
        
        if (e - s + 1) >= 3:
            res.append([s, e])
        
        return res

                
        