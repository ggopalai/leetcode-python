#keep track of the previous ending time after sorting. when there is an overlap, remove the one that ends last == just set the prevEnd to one that 
# ends earlier.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0
        
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        
        return res