class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i, j, result = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result
