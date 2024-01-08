class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        left = 0
        right = 0
        zeros = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                zeros += 1

            while left <= right and zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
        