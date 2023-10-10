class Solution:
    def subarraysDivByK(self, nums, k):
        lst = [0]*k
        total = 0
        for num in nums:
            total += num
            lst[total % k] += 1
        result = lst[0]
        for mod in lst:
            result += (mod*(mod-1)) // 2
        return result