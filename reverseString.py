class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[-1:-len(s)-1:-1]
        