class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        track = {0:1}

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        ans = 0

        for i in nums:
            diff = i - k
            if diff in track:
                ans += track[diff]

            track[i] = track.get(i, 0) + 1

        return ans
        