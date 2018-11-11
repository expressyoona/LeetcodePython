class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(M)
        cols = len(M[0])
        result = []
        
        for i in range(rows):
            row = []
            for j in range(cols):
                Sum, ctr = M[i][j], 1
                if i >= 1:
                    Sum += M[i-1][j]
                    ctr += 1
                    if j >= 1:
                        Sum += M[i-1][j-1]
                        ctr += 1
                    if j + 1 < cols:
                        Sum += M[i-1][j+1]
                        ctr += 1
                if j >= 1:
                    Sum += M[i][j-1]
                    ctr += 1
                    if i + 1 < rows:
                        Sum += M[i+1][j-1]
                        ctr += 1
                if i + 1 < rows:
                    Sum += M[i+1][j]
                    ctr += 1
                if j + 1 < cols:
                    Sum += M[i][j+1]
                    ctr += 1
                    if i + 1 < rows:
                        Sum += M[i+1][j+1]
                        ctr += 1
                row.append(int(Sum / ctr))
            result.append(row)
            
        return result