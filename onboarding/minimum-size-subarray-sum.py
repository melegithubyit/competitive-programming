class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        flag = False

        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while left <= right and current_sum >= target:
                min_length = min(min_length, right - left + 1)
                flag = True
                current_sum -= nums[left]
                left += 1


        if flag:return min_length
        return 0
