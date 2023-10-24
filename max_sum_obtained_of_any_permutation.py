class Solution:
    def maxSumRangeQuery(self, nums, requests) -> int:

        counter = [0] * (len(nums) + 1)
        x = int(1e9) + 7

        for left, right in requests:
            counter[left] += 1
            counter[right + 1] -= 1

        cumulative = [0] * len(nums)
        cumulative[0] = counter[0]

        for i in range(1, len(nums)):
            cumulative[i] = cumulative[i - 1] + counter[i]

        nums.sort(reverse=True)
        cumulative.sort(reverse=True)

        max_total = 0

        for i in range(len(nums)):
            max_total = (max_total + nums[i] * cumulative[i]) % x

        return max_total
