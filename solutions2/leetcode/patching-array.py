class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        index = 0
        upto = 0
        patch_count = 0
        N = len(nums)

        while upto < n:

            if index < N and nums[index] <= upto + 1:
                upto += nums[index]
                index += 1
            
            else:
                patch_count += 1
                upto += (upto + 1)

        
        return patch_count
