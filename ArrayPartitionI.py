class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        S = 0
        for i in range(0, len(nums), 2):
            S += nums[i]
        return S