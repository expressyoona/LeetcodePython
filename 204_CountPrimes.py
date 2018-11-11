class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        Max = n
        primes = [True] * n
        
        primes[0] = False
        primes[1]= False
        n = int(n ** 0.5)
        for i in range(n+1):
            if primes[i]:
                for j in range(2 * i, Max, i):
                    primes[j] = False
        #print(primes)
        return primes.count(True)
