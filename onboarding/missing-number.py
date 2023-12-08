class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = 0
        for i in range(n+1):
            prefix_sum += i
        
        current_sum = sum(nums)
        return prefix_sum - current_sum
        