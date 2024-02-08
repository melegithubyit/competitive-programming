class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        store = {0:1}
        ans = 0

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in nums:
            diff = i - goal

            if diff in store:
                ans += store[diff]
            
            store[i] = store.get(i, 0) + 1
        
        return ans

