class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        i = 0
        while (nums[i] < target):
            i += 1
        return i
        
