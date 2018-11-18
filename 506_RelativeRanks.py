class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        temp = sorted(nums, reverse = True)
        result = []
        for score in nums:
            rank = temp.index(score)
            if rank == 0:
                result.append('Gold Medal')
            elif rank == 1:
                result.append('Silver Medal')
            elif rank == 2:
                result.append('Bronze Medal')
            else:
                result.append(str(rank + 1))
        return result
