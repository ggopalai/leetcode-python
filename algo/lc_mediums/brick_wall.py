class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        d = defaultdict(int)

        r, c = len(wall), sum(wall[0])
        
        temp = [[] for _ in range(r)]

        for i in range(r):
            for j in range(len(wall[i])):
                if j == 0:
                    temp[i].append(wall[i][0])
                else:
                    temp[i].append(temp[i][j - 1] + wall[i][j])
        
        for i in range(r):
            for j in temp[i]:
                if j != c:        
                    d[j] += 1
        
        if not d:
            return r

        maxLine = max([v for v in d.values()])
        
        return r - maxLine