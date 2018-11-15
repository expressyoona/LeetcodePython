class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        line = [1]
        for i in range(rowIndex):
            line.append(line[i] * (rowIndex - i) // (i + 1))
        return line
