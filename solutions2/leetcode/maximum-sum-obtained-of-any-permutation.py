class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        lst = [0] * n
        MOD = 10**9 + 7

        for i in requests:
            start, end = i
            lst[start] += 1
            if end < n - 1:
                lst[end + 1] -= 1
        
        for i in range(1, n):
            lst[i] += lst[i-1]
        
        nums.sort()
        lst.sort()
        ans = 0

        for i in range(n):
            ans += nums[i] * lst[i]

        return ans % MOD

       




        