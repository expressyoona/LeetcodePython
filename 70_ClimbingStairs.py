class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        L = []
        L.append(1)
        L.append(2)
        for i in range(2, n + 1):
            #print(i)
            L.append(L[i-1] + L[i-2])
        return L[n-1]
