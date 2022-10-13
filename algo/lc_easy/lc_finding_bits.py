"""
https://leetcode.com/problems/counting-bits/
"""
class Solution:
    def count(self, n: int) -> int:
        a = bin(n)[2:]
        count = 0
        for i in a:
            if i == '1':
                count += 1
        return count 
    
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n+1):
            res.append(self.count(i))
        return res

# this works, but check for a more optimal solution. 

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n+1):
            res.append(bin(i)[2:].count('1'))
        return res