class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good_ptr = len(nums) - 1

        for i in range(len(nums) - 2 , -1 , -1):
            if i + nums[i] >= good_ptr:
                good_ptr = i

        return good_ptr == 0
