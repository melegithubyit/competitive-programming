class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        prefix[0] = float('inf')
        suffix[-1] = float('-inf')

        n = len(nums)
        min_val_prefix = nums[0]
        max_val_suffix = nums[-1]
        counter = 0

        for i in range(1, n):
            prefix[i] = min_val_prefix
            min_val_prefix = min(min_val_prefix, nums[i])

        for i in range(n - 2, -1, -1):
            suffix[i] = max_val_suffix
            max_val_suffix = max(max_val_suffix, nums[i])

        for i in range(n):
            if nums[i] > prefix[i] and nums[i] < suffix[i]:
                counter += 1

        if counter >= 1:
            return True
        return False
        






        
        