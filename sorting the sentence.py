class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        test = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    counter += 1
            test.append(counter)

        return test


