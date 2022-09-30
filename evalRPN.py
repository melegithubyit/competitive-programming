class Solution:
    def evalRPN(self, tokens):
        stk = []
        for i in tokens:
            if i == "+":
                stk.append(stk.pop() + stk.pop())
            elif i == "*":
                stk.append(stk.pop() * stk.pop())

            elif i == "/":
                m= stk.pop()
                n= stk.pop()
                stk.append(int(n / m))
            elif i == "-":
                m, n = stk.pop(), stk.pop()
                stk.append(int(n - m))
            else:
                stk.append(int(i))
        return stk[0]

trial=Solution()
token=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(trial.evalRPN(token))