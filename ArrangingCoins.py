class Solution:
    def arrangeCoins(self, n):
        i = 0
        ctr = 0
        while(i < n):
            if n - i >= 0:
                ctr = ctr + 1
                i = i + 1
                n = n - i
        return ctr
        #:type n: int
        #:rtype: int
        
        