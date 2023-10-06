class Solution:
    def merge(intervals):
        intervals.sort()
        result = []
        result.append(intervals[0])
        for i in intervals[1:]:
            if result[-1][0] <= i[0] <= result[-1][-1]:
                result[-1][-1] = max(result[-1][-1], i[-1])
            else:
                result.append(i)
        return result
