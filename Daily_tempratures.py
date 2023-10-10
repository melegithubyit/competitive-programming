class Solution:
    def dailyTemperatures(self, temperatures):
        stk = []
        n = len(temperatures)
        result = [0] * n
        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                top = stk.pop()
                result[top] = i - top

            stk.append(i)

        return result
