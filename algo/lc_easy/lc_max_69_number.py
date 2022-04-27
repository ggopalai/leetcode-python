# https://leetcode.com/problems/maximum-69-number/

def maximum69Number (self, num: int) -> int:
        a = str(num)
        if a.find('6') == -1:
            return num
        else:
            a = a.replace('6', '9', 1)
        
        return int(a)