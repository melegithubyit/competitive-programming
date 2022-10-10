class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        if len(nums) < secondLen + firstLen:
            return 0
        else:
            for i in range(1, len(nums)):
                nums[i] += nums[i - 1]
            result, maxf, maxs = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
            for i in range(firstLen + secondLen, len(nums)):
                maxf = max(maxf, nums[i - secondLen] - nums[i - secondLen - firstLen])
                maxs = max(maxs, nums[i - firstLen] - nums[i - firstLen - secondLen])
                result = max(result, maxf + nums[i] - nums[i - secondLen], maxs + nums[i] - nums[i - firstLen])
            return result
