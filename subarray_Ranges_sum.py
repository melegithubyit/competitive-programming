class Solution:
    def subArrayRanges(self, nums):
        if not nums:
            return
        counter = 0
        n = len(nums)
        for left in range(n):
            max_val = float('-inf')
            min_val = float('inf')
            for right in range(left, n):
                max_val = max(max_val, nums[right])
                min_val = min(min_val, nums[right])
                counter += max_val - min_val

        return counter
