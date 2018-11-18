class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for i in cost[::-1]:
            f1, f2 = i + min(f1, f2), f1
        return min(f1, f2)
        
