class Solution(object):
    
    
    def maxAreaOfIsland(self, A):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def visit(i, j):
            count = 0
            if A[i][j] == 1:
                A[i][j] = 0
                count += 1
                if i - 1 >= 0:
                    if A[i-1][j] == 1:
                        count += visit(i-1, j)
                if j - 1 >= 0:
                    if A[i][j-1] == 1:
                        count += visit(i, j-1)
                if i + 1 < len(A):
                    if A[i+1][j] == 1:
                        count += visit(i+1, j)
                if j + 1 < len(A[0]):
                    if A[i][j+1] == 1:
                        count += visit(i, j+1)
                return count
            
        Max = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    temp = visit(i, j)
                    if temp > Max:
                        Max = temp
        return Max
