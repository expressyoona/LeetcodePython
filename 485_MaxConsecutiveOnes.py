class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ctr, Max = 0, 0
        for i in nums:
            if i == 1:
                ctr += 1
            else:
                if ctr > Max:
                    Max = ctr
                ctr = 0
        return Max if Max > ctr else ctr
