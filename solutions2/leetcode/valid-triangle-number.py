class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
         
        nums.sort()
        n = len(nums)
        result = 0

        for slow in range(2, n):
            left = 0
            right = slow - 1

            while left < right:
                if nums[left] + nums[right] > nums[slow]:
                    result += (right - left)
                    right -= 1
                else:
                    left += 1
        
        return result
        