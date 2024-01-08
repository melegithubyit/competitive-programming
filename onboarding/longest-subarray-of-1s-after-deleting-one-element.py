class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        left = 0
        right = 0
        zeros = 0


        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1
            
            while left < right and zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            longest = max(longest, right - left)


        return longest


