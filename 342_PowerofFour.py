class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        return (math.log10(num) / math.log10(4.0)) % 1 == 0