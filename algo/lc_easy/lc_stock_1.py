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