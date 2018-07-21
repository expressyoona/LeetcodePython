class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ctr = 0
        for i in S:
            if i in J:
                ctr += 1
        return ctr
