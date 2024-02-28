class Solution(object):
    def permute(self, nums):
        
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0)
        return result