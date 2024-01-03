class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        left = 0
        right = len(nums) - 1
        ans = 0

        while left < right:
            total = nums[left] + nums[right]

            while left < right and total >= target:
                right -= 1
                total = nums[left] + nums[right]

            ans += (right - left)

            
            left += 1
        
        return ans
        