class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n):
            c = n - 1 - i
            if digits[c] == 9:
                digits[c] = 0
            else:
                digits[c] += 1
                return digits
        
        return [1] + digits
        