class Solution:
    def reverseParentheses(self, s):
        size = len(s)
        stk = []   #initating a new stack
        for i in range(size):
            if s[i] == '(':
                stk.append(i)
            elif s[i] == ')':
                new = s[stk[-1]: i + 1]
                s = s[:stk[-1]] + new[::-1] + s[i + 1:]
                del stk[-1]

        result = ''
        for i in s:
            if i != '(' and i != ')':
                result += i
        return result
