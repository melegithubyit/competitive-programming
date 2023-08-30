class Solution:
    def intersection(self, nums1, nums2):
        output = []
        total = nums1 + nums2
        for i in total:
            if i in nums1 and i in nums2 and i not in output:
                output.append(i)
        return output
