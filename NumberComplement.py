class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        st = bin(num)[2::]
        st = st.replace('0', '*')
        st = st.replace('1', '0')
        st = st.replace('*', '1')
        return int(st, 2)