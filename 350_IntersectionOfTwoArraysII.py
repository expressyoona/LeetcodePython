class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        L = []
        L1 = set(nums1)
        L2 = set(nums2)
        for num in L1:
            if num in L2:
                L.append(num)
        return L
