class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        st = bin(n)
        st = st[2::]
        for i in range(0,len(st)-1):
            if st[i] == st[i+1]:
                return False
        return True
