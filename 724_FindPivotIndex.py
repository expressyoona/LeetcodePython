class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        S_left = 0
        i = 0
        while i < len(nums):
            S_left += nums[i]
            S -= nums[i]
            if S_left - nums[i] == S:
                return i
            i += 1
        return -1
            
