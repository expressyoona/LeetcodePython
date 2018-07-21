class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        L = {6, 28, 496, 8128, 33550336}
        return num in L
