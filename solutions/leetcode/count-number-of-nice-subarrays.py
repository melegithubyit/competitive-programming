class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for idx, ele in enumerate(nums):
            if ele % 2 == 0:
                nums[idx] = 0
            else:
                nums[idx] = 1

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        store = {0 : 1}
        answer = 0

        for i in nums:
            val = i - k

            if val in store:
                answer += store[val]
                # store[val] += 1
            
            store[i] = store.get(i, 0) + 1

        return answer