class Solution:
    def sortArrayByParity(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] % 2 != 0 and nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 != 0:
                right -= 1
        return nums
