class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            nums[i] %= k

        track = {0:1}
        count = 0

        for i in nums:
            if i in track:
                count += track[i]
                track[i] += 1
            
            else:
                track[i] = track.get(i, 0) + 1

        return count

        