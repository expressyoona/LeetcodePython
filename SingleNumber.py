class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        kq = 0
        for i in nums:
            kq = kq ^ i
        return kq