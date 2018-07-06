class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L = []
        visited = set()
        for num in nums1:
            if num not in visited:
                f = nums1.count(num)
                s = nums2.count(num)
                if f <= s:
                    L = L + [num] * f
                if f > s:
                    L = L + [num] * s
                visited.add(num)
        return L