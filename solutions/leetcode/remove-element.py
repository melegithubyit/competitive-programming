class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        hold = 0
        seek = len(nums) - 1
        while hold <= seek:
            if nums[hold] == val:
                nums[hold], nums[seek] = nums[seek], nums[hold]
                seek -= 1
            else:
                hold += 1
                
        return hold