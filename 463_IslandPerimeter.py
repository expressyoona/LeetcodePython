class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = len(grid[0])
        row = len(grid)
        P = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    #A[i][j] --> i là hàng, j là cột
                    #Với mỗi A[i][j] thì kiểm tra A[i][j-1] A[i+1][j] A[i][j+1] A[i-1][j]
                    if j - 1 < 0:
                        P += 1
                    elif grid[i][j-1] == 0:
                        P += 1
                    if i + 1 == row:
                        P += 1
                    elif grid[i+1][j] == 0:
                        P += 1
                    if j + 1 == col:
                        P += 1
                    elif grid[i][j+1] == 0:
                        P += 1
                    if i - 1 < 0:
                        P += 1
                    elif grid[i-1][j] == 0:
                        P += 1
        return P
