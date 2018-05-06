class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = 0
        n = x
        while x != 0:
            temp = temp * 10 + x % 10
            x = x // 10
        return temp == n
        
