class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0, int(math.sqrt(c))+1):
            temp = c - i * i
            j = int(math.sqrt(temp))
            if i*i + j*j == c:
                return True
        return False
