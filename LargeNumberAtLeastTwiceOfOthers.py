class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        for i in nums:
            if 2*i > max_num and i != max_num:
                return -1
        return nums.index(max_num)
        