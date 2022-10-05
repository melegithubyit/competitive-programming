class Solution(object):
    def rotate(self, nums, k):
        list=[]
        for i in range(1,k+1):
            list.insert(0,nums[len(nums)-i])
        for j in range(0,len(nums)-k):
            list.append(nums[j])

        return list
