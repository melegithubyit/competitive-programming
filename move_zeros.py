class Solution:
    def moveZeroes(nums):
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index] = nums[i]
                zero_index += 1
        for i in range(zero_index, len(nums)):
            nums[i] = 0
