class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def DIST(nums):
            n = len(nums)
            psum = [0] * (n+2)
            psum[1] = nums[0]
            for i in range(1, n):
                psum[i+1] += nums[i] + psum[i]

            ans = []
            for i, num in enumerate(nums):
                left = nums[i] * i - psum[i] 
                right = psum[-2] - psum[i+1] - (n-i-1) * nums[i]
                dist = left + right
                ans.append(dist)
            
            return ans

        store = defaultdict(list)
        for i in range(len(nums)):
            store[nums[i]].append(i)

        for key, value in store.items():
            store[key] = DIST(value)

        ans = [0] * len(nums)
        for j in range(len(nums) - 1, -1, -1):
            a = store[nums[j]]
            ans[j] = a[-1]
            store[nums[j]].pop()

        return ans