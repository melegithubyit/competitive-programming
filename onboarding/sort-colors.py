class Solution:
    def sortColors(self, nums: List[int]) -> None:
        slow = 0
        fast = 0

        while slow < len(nums):
            
            fast = slow
            curr_min_index = fast
            while fast < len(nums):
                if nums[fast] < nums[curr_min_index]:
                    curr_min_index = fast
                fast += 1
            nums[slow], nums[curr_min_index] = nums[curr_min_index], nums[slow]
            slow += 1

        return nums

            