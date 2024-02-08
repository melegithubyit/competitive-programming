class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prod = [0] * n
        right_prod = [0] * n

        left_prod[0] = 1
        right_prod[-1] = 1

        for i in range(1, n):
            left_prod[i] = nums[i-1] * left_prod[i-1]
            right_prod[n-i-1] = nums[n-i] * right_prod[n-i]

        for i in range(n):
            nums[i] = left_prod[i] * right_prod[i]

        return nums 
        