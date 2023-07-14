class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        min_length = float('inf')
        current_sum = 0
        start = 0

        for end in range(len(nums)):
            current_sum += nums[end]

            while current_sum >= target:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]
                start += 1

        return min_length if min_length != float('inf') else 0
