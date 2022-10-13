# 1. Hardcoding solution. 
class Solution:
    def intToRoman(self, num: int) -> str:
        m = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], 
             ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400],
             ['D', 500], ['CM', 900], ['M', 1000]]
        res = ""
        for sym, val in reversed(m):
            if num // val:
                dig = num // val #this tells how many of that unit is needed
                num = num % val #work on the remaining digits
                res += (dig * sym) #append to result
        
        return res

