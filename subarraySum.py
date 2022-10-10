class Solution:
    def subarraySum(self, nums, k):
        sumdic = {0: 1}
        total = 0
        counter = 0
        for i in nums:
            total += i
            if total - k in sumdic:
                counter += sumdic[total - k]
            if total in sumdic:
                sumdic[total] += 1
            else:
                sumdic[total] = 1
        return counter
