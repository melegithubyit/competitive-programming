class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        nums.insert(len(nums), target)
        nums.sort()
        return nums.index(target)
