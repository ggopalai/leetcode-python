# leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = dict()
        
        for i in t:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in s:
            d[i] -= 1
            
        for k, v in d.items():
            if v == 1:
                return k
        
        