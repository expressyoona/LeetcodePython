class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        L = [0] * 26
        for i in range(len(s)):
            L[ord(s[i]) - 97] += 1
            L[ord(t[i]) - 97] -= 1
        for i in L:
            if i != 0:
                return False
        return True