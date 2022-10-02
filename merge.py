class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        stk = []
        stk.append(intervals[0])
        for i in intervals[1:]:
            if stk[-1][0] <= i[0] <= stk[-1][-1]:
                stk[-1][-1] = max(stk[-1][-1], i[-1])
            else:
                stk.append(i)
        return stk