class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        nums = [i for i in range(1, 10)]

        def backtrack(nums, k, n, arr):
            if sum(arr) == n and len(arr) == k:
                result.append(arr[:])
                return 

            elif sum(arr) > n or len(arr) > k:
                return 
            
            for i in range(len(nums)):
                arr.append(nums[i]) 
                backtrack(nums[i+1:], k, n, arr)
                arr.pop()
            
        backtrack(nums, k, n, [])
        return result

        