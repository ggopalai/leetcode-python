import bisect 
from typing import List
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        indices = [i for i, c in enumerate(s) if c == '|']
        res = []
        for left, right in queries:
            # position of the first candle 
            l = bisect.bisect_left(indices, left)
            # position of the right most candle in the given substring 
            r = bisect.bisect_right(indices, right) - 1
            if l < r:
                # distance between the candles
                lengthBetweenCandles = indices[r] - indices[l] + 1
                numCandles = r - l + 1 # total candles in between the chosen positions 
                res.append(lengthBetweenCandles - numCandles)
            else:
                res.append(0)
        
        return res
