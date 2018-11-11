class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows = len(nums)
        cols = len(nums[0])
        result = []
        if rows * cols != r * c:
            return nums
        ctr = 0
        row = []
        for i in range(rows):
            for j in range(cols):
                row.append(nums[i][j])
                ctr += 1
                if ctr == c:
                    result.append(row)
                    row = []
                    ctr = 0
        return result
