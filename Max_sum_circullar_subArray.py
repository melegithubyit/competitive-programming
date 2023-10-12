from itertools import accumulate

class Solution:
    def maxSubarraySumCircular(self, nums):
        ans = current_sum = nums[0]
        m = len(nums)
        for i in range(1, m):
            current_sum = max(nums[i], nums[i]+current_sum)
            ans = max(ans, current_sum)

        A = list(accumulate(nums))
        B = list(accumulate(nums[::-1]))[::-1]
        A_max = list(accumulate(A, max))
        B_max = list(accumulate(B[::-1], max))[::-1]
        B_max.append(0)
        n = len(A_max)
        for i in range(n):
            ans = max(ans, A_max[i]+B_max[i+1])
        return ans
