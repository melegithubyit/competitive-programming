class Solution:
    def maxSubArray(self, nums) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])
            maxSum = max(maxSum, currentSum)

        return maxSum
