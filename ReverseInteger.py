class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31 - 1 or x < (-1)*2**31:
            return 0
        if x > 0:
            st = str(x)
            if int(st[::-1]) > 2**31 - 1 or int(st[::-1]) < (-1)*2**31:
                return 0
            else:
                return int(st[::-1])
        else:
            st = str(x*(-1))
            if (-1)*int(st[::-1]) > 2**31 - 1 or (-1)*int(st[::-1]) < (-1)*2**31:
                return 0
            else:
                return (-1)*int(st[::-1])
        
        