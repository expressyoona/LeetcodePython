class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = 0
        Max = float('-inf')
        for i in range(len(nums)):
            S += nums[i]
            if Max < S:
                Max = S
            if S < 0:
                S = 0
        return Max
