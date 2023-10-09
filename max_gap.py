class Solution(object):
    def maximumGap(self, nums):
        nums.sort()
        new = []
        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                new.append(abs(nums[i]-nums[j]))
                break

        return max(new)
