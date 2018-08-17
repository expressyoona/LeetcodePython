class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = set(nums)
        n = len(nums)
        result = []
        for num in range(1,n+1):
            if num not in L:
                result.append(num)
        return result
