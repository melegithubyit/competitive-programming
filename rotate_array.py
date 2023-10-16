class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
