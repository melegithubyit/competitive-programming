class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def compute(x,y,op):
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op == '*':
                return x*y
            else:
                if x*y < 0:
                    x *= -1
                    val = x // y
                    return -val

                val = x // y
                return val


        stack = []
        operations = {'+','-','*','/'}

        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                oper1 = int(stack.pop())
                oper2 = int(stack.pop())
                res = compute(oper2, oper1, i)
                stack.append(res)
            # print(stack)

        return int(stack[0])




        