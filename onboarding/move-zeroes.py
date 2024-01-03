class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        hold = 0
        seek = 0

        while hold < len(nums):
            if nums[hold] != 0:
                hold += 1
                seek = hold
            else:
                while seek < len(nums):
                    if nums[seek] != 0:
                        nums[seek], nums[hold] = nums[hold], nums[seek]
                        hold += 1
                        break
                    seek += 1
                else:
                    hold += 1