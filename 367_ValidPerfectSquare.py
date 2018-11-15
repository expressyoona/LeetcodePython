class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        S, i = 1, 1
        while S < num:
            i += 2
            S += i
        return S == num
