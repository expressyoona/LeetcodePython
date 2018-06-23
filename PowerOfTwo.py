class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1 or n == 2:
            return True
        while (n != 1):
            if n % 2 != 0:
                return False;
            else:
                n = n / 2
        return True;