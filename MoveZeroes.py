class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ctr = nums.count(0)
        while nums.count(0) != 0:
            nums.remove(0)
        for i in range(ctr):
            nums.append(0)