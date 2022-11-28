class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in intervals:
            #if new interval is to the left of the current interval
            if newInterval[1] < i[0]:
                res.append(newInterval)
                return res + intervals[intervals.index(i):]
            #new interval is to the right of the current interval
            elif newInterval[0] > i[1]:
                res.append(i)
            #there is an overlap
            else:
                newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]
        
        #for the cases where the merged interval is in the of the list, add that here.
        res.append(newInterval)
        
        return res
                
                    
                    