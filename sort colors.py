class Solution(object):
    def sortColors(self,nums):
        pt1 = 0
        pt2 = len(nums) - 1
        pt3 = 0
        def swap(pt3,i):
            temp = nums[pt3]
            nums[pt3]= nums[i]
            nums[i] = temp
        while pt3 <= pt2:
            if nums[pt3]== 0:
                swap(pt1,pt3)
                pt1 += 1
            elif nums[pt3] == 2:
                swap(pt3,pt2)
                pt2 -=1
                pt3 -=1
            pt3 += 1