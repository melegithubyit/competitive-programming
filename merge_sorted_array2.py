class Solution:
    def merge(nums1,m, nums2, n) -> None:
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - (m-n) - n]
        for i in range(len(nums1) - 1):
            min_index = i
            for j in range(i+1, len(nums1)):
                if nums1[j] < nums1[min_index]:
                    min_index = j
            nums1[min_index], nums1[i] = nums1[i], nums1[min_index]
