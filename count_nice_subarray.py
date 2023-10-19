class Solution:
    def numberOfSubarrays(self, nums, k):
        counter, number = 0, 0
        list = [0] * (len(nums)+1)
        for i in range(len(nums)):
            list[number] += 1
            if (nums[i] % 2 == 1):
                number += 1
            if (number >= k):
                counter += list[number - k]

        return counter
