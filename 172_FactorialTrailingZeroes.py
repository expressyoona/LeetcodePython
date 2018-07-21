class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ctr = 0
        i = 5
        while n // i >= 1:
            ctr += n // i
            i *= 5
        return ctr
