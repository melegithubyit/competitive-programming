class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total = sum(nums)
        remainder = total % p
        if remainder == 0:
            return 0

        store = { 0 : -1 }
        prefix = 0
        min_len = len(nums)
        
        for idx, num in enumerate(nums):
            prefix += num
            prefix %= p
            target = (prefix - remainder + p) % p
            if target in store:
                min_len = min(min_len, idx - store[target])
            
            store[prefix] = idx


        
        return -1 if min_len == len(nums) else min_len