class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        list = [nums[0]]
        for i,j in enumerate(nums):
            if i > 0:
                list.append(list[i-1]+j)
            if list[i]-j == total-list[i]:
                return i
        return -1
