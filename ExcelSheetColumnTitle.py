class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        if n <= 26:
            return chr(ord('A') - 1 + n % 27)
        while n > 0:
            ch = (n - 1) % 26
            result = chr(ord('A') + ch) + result
            n = (n-1) // 26
        return result