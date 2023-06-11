import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        primes = [True] * (n+1)
        primes[0] = False
        primes[1] = False

        for i in range(2,int(math.sqrt(n))+1):
            if primes[i]:
                for j in range(i*i,n,i):
                    primes[j] = False
                
        return(len([i for i in range(2,n) if primes[i]]))




