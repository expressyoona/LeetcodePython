class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        S = int(l*(l+1)/2)
        Sum = 0
        for i in nums:
            Sum += i
        return S - Sum
        
