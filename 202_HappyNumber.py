class Solution:
    def sqrSum(self, n):
        S = 0
        while n:
            S += (n % 10) ** 2
            n = n // 10
        return S
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n
        while True:
            slow = self.sqrSum(slow)
            fast = self.sqrSum(self.sqrSum(fast))
            if slow == fast:
                break
        return slow == 1
        
