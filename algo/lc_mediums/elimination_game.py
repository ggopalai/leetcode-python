# 3375 / 3377 test cases passed. 2 MLE.
class Solution:
    def lastRemaining(self, n: int) -> int:
        og = [i for i in range(1, n + 1)]
        c = 1
        while len(og) > 1:
            temp = []
            if c % 2 == 1:
                for i in range(1, len(og), 2):
                    temp.append(og[i])
            else:
                for i in range(len(og) - 2, -1, -2):
                    temp.append(og[i])
                temp.reverse()
            
            og = temp
            c += 1
        
        return og[0]
    
# Recursion and math logic for log n solution. 