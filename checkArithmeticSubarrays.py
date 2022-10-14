class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        n=len(r)
        new_list = [True] * n
        for i in range(n):
            data = nums[l[i]:r[i] + 1]
            data.sort()

            array = []
            for j in range(len(data) - 1):
                array.append(data[j + 1] - data[j])
                array = list(set(array))
                if len(array) != 1:
                    new_list[i] = False
        return new_list














