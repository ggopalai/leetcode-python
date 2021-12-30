# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
def numberOfSteps(self, num: int) -> int:
        x = num 
        count = 0
        while x:
            if x % 2 == 0:
                x /= 2
            else:
                x -= 1
            count += 1
        
        return count 

