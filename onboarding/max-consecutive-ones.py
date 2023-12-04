class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_val = 0
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] == 1:
                max_val = max(max_val, right - left + 1)
                right += 1
            
            else:
                right += 1
                left = right

        return max_val



        