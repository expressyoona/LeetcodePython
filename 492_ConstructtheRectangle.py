class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        Require:
        1. L * W = area
        2. L >= W
        3. L - W = MIN
        """
        for i in range(int(math.sqrt(area)), 0, -1):
            if area % i == 0:
                return [max(area // i, i), min(area // i, i)]
