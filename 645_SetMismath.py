class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        S = sum(set(nums))
        length = len(nums)
        SUM = length * (length + 1) // 2
        return [sum(nums) - S, SUM - S]
