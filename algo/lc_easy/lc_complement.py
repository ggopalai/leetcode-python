# https://leetcode.com/problems/number-complement/

def findComplement(self, num: int) -> int:
        a = bin(num)[2:]
        res = ''
        for i in a:
            if i == '1':
                res += '0'
            else:
                res += '1'
        
        return int(res, 2)


# follow up with a solution using bitwise operators? 

