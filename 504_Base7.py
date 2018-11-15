class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        nega = False
        result = ""
        if num == 0:
            return '0'
        if num < 0:
            num = - num
            nega = True
        
        while num:
            result = str(num % 7) + result
            num = num // 7
        
        return result if not nega else '-' + result
