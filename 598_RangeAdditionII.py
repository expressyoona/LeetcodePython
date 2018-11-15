class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        #Tìm  và 
        if len(ops) == 0:
            return m * n
        MinX, MinY = float('inf'), float('inf')
        for rows in ops:
            #print(MinX, MinY)
            MinX = min(MinX, rows[0])
            MinY = min(MinY, rows[1])
        return (MinX) * (MinY)
