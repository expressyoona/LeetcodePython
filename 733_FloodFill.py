class Solution:
    def floodFill(self, A, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        value = A[sr][sc]
        if value == newColor:
            return A
        def fill(i, j):
            if A[i][j] == value:
                A[i][j] = newColor
                if i >= 1: fill(i-1, j)
                if j >= 1: fill(i, j-1)
                if i+1 < rows: fill(i+1, j)
                if j+1 < cols: fill(i, j+1)
        fill(sr, sc)
        return A