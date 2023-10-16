class Solution:
    def longestSubarray(self, nums) -> int:
        length = len(nums)
        left = 0
        max_value = 0
        zero_count = 0

        for right in range(length):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_value = max(max_value, right - left)

        return max_value




        