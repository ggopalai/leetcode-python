class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [0, 0] + [1] * (n-2)
        
        for i in range(2, int(math.sqrt(n))+1):
            if primes[i]:
                for j in range(i * i, n, i): # i * i will give least calculations. can do 2 * i also. 
                    primes[j] = 0
                    
        return sum(primes) 
    
