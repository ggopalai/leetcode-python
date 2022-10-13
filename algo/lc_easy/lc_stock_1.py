# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

import sys 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = sys.maxsize
        p = 0
        
        for i in prices:  # at each value, either 1. update minimum or 2. update profit 
            if i < m:
                m = i
            if i - m > p:
                p = i - m
        
        
        return p


#own solution without help on 24/7/22
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 10001
        prof = 0
        
        for i in prices:
            if i < m:
                m = i
            else:
                prof = max(prof, i - m)
        
        return prof
                