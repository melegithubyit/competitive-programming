class Solution:
    def maxOperations(self, nums, k):
        nums.sort()
        counter = 0
        i=0
        j=len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == k:
                counter += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        return counter

