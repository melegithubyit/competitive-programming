class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        i,j,m,result= 0,0,0,0
        for m in range(len(nums)):
            j += nums[m]
            while ((m - i + 1) * nums[m] - j > k):
                j -= nums[i]
                i += 1
            result = max(result, m - i + 1)
        return result