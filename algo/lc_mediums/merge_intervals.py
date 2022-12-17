class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        res = [intervals[0]]
        
        for start, end in intervals[1: ]:
            lastEnding = res[-1][1]
            
            if start <= lastEnding:
                res[-1][1] = max(end, lastEnding)
            else:
                res.append([start, end])
        
        return res
        