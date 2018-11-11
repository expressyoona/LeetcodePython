class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        st = ''.join(S.split('-')).upper()
        result = []
        for i in range(len(st), -1, -K):
            if i - K >= 0:
                result.append(st[i-K:i])
            else:
                result.append(st[:i])
        if result[-1] == '':
            result.pop(-1)
        return '-'.join(result[::-1])