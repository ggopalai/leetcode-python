class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        cap = int(math.sqrt(num))
        factors = []
        for i in range(1, cap + 1):
             if num % i == 0:
                 factors.extend([i, num // i])
        
        total = 0
        for i in factors:
            if i != num:
                total += i

        return True if total == num else False

