class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        L = list(s)
        for i in range(0, len(L), 2 * k):
            L[i:i + k] = reversed(L[i:i+k])
        return "".join(L)
