class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        result = ''
        hexa = '0123456789abcdef'
        
        if num < 0:
            num += 2 ** 32
        
        while num > 15:
            result = hexa[num % 16] + result
            num //= 16
        
        result = hexa[num] + result
        
        return result
