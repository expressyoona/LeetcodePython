class Solution:
    def isPrime(self, n):
        if (n < 2):
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    def countSetBits(self, n):
        return bin(n).count('1')
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        ctr = 0
        for i in range(L, R+1):
            if self.isPrime(self.countSetBits(i)):
                ctr = ctr + 1
        return ctr
