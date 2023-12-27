class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # or may be optimazing using two pointers
        nums1.sort()
        nums2.sort()

        pt1 = 0
        pt2 = 0

        n = len(nums1)
        m = len(nums2)
        ans = []

        while pt1 < n and pt2 < m:
            if nums1[pt1] == nums2[pt2]:
                ans.append(nums1[pt1])
                pt1 += 1
                pt2 += 1
            
            elif nums1[pt1] > nums2[pt2]:
                pt2 += 1
            
            else:
                pt1 += 1

        return ans

