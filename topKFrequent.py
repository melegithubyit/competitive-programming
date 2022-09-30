import collections
class Solution:
    def topKFrequent(self, nums, k):
        y = collections.Counter(nums)
        output = []
        for num in y:
            output.append([num, y[num]])
        output.sort(key=lambda x: x[1], reverse=True)
        final = []
        for i in range(k):
            final.append(output[i][0])
        return final
