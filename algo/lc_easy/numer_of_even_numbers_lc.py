from typing import List

def counter(num: int) -> bool:
        count = 0
        while num > 0:
            count += 1
            num //= 10 #flooring division 
            
        if count % 2 == 0:
            return True
        
        return False
        
def findNumbers(nums: List[int]) -> int:
    count = 0
    for i in nums:
        if counter(i):
            count += 1
            
    return count


#alternative solution - convert int to str and % the length. Super cool, never thought of this! ;) 