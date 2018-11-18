class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #L = 0
        if not nums:
            return 0
        
        
        L = len(nums)
        if L == 1:
            return nums[0]
        if L == 2:
            return max(nums)
        total = []
        
        #L = 1
        total.append(nums[0])
        #L = 2
        total.append(max(nums[0], nums[1]))
        Max = 0
        for i in range(2, L):
            value = max(total[i - 2] + nums[i], total[i - 1])
            if value > Max:
                Max = value
            total.append(value)
        return Max
        
            
