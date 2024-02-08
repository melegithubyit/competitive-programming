class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        total = 0

        for i in nums:
            if total < 0:
                total = 0

            total += i
            max_sum = max(max_sum, total)

        return max_sum




