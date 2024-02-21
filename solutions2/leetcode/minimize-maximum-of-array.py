class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        if nums[0] == max(nums):
            return max(nums)
        
        max_val = float('-inf')
        total_sum = 0

        for i in range(len(nums)):
            total_sum += nums[i]
            current_max = math.ceil(total_sum / (i+1))
            max_val = max(max_val, current_max)

        return max_val

            