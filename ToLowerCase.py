class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = ""
        for letter in str:
            if 'A' <= letter <= 'Z':
                result = result + chr(ord(letter) + 32)
            else:
                result = result + letter
        return result