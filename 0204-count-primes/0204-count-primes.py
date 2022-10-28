class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        primes = [True]*(n)  
        for i in range(2,math.isqrt(n)+1):
            multiplier = 2
            if primes[i]:
                j = i
                while j*i < n:
                    primes[j * i] = False
                    j+=1
        return sum(primes) - 2
                
            
            
        