class Solution:
    def validateStackSequences(self, pushed):
        stack = []
        j = 0
        N = len(popped)
        for x in pushed:
            stack.append(x)
            while stack and j < N and stack[-1] == popped[j]:
                j += 1
                stack.pop()
        return j == len(popped)