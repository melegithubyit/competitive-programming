class Solution:
    def findLength(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        lst = [[0]*(n+1) for _ in range(m+1)]
        result = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if nums1[i] == nums2[j]:
                    lst[i][j] = 1 + lst[i+1][j+1]
                result = max(result, lst[i][j])
        return result
