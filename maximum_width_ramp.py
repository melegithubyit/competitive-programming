class Solution:
    def maxWidthRamp(self, nums):
        stack = []
        n = len(nums)
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        max_width = 0
        for j in range(n-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                top = stack.pop()
                max_width = max(max_width, j - top)
        return max_width
