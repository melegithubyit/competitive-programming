class Solution:
    def nextGreaterElement(self, nums1, nums2):
        result = []
        for i in nums1:
            m = -1
            for j in range(nums2.index(i), len(nums2)):
                if(nums2[j]>i):
                    m=nums2[j]
                    break
            result.append(m)
        return result