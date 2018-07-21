class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        S = 0
        for letter in s:
            S = S * 26 + ord(letter) - 65 + 1
        return S
