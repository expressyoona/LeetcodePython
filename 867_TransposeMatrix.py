class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        L = []
        row = len(A)
        col = len(A[0])
        for i in range(col):
            r = []
            for j in range(row):
                r.append(A[j][i])
            L.append(r)
        return L
