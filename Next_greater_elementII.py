class Solution:
    def nextGreaterElements(self, nums):
        Nums = nums + nums
        stk = list()
        greater = dict()
        for i in range(len(Nums)):
            n = Nums[i]
            while stk and stk[-1][0] < n:
                greater[stk[-1][1]] = n
                stk.pop()
            stk.append([n, i])
        result = list()
        for i in range(len(nums)):
            if i not in greater:
                result.append(-1)
            else:
                result.append(greater[i])
        return result
