class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i, Max = 0, A[0]
        for num in range(1, len(A)):
            if A[num] > Max:
                Max = A[num]
                i = num
        return i
