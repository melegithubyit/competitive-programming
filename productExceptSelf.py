class Solution:
    def productExceptSelf(self, nums):
        (inital,counter) = (1,1)
        list = [1]
        for i in range(len(nums) - 1):
            inital *= nums[i]
            list.append(inital)

        for j in range(len(nums) - 1, -1, -1):
            list[j] *= counter
            counter *= nums[j]
        return list




