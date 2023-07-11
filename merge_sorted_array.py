class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for item in nums2:
            indexOf_zero = nums1.index(0)
            nums1[indexOf_zero] = item
        nums1.sort()
