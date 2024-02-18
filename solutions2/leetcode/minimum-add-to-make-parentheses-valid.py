class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        depth = 0
        stk = []

        for i in s:
            if not stk:
                stk.append(i)
                depth += 1
            else:
                if i == '(':
                    depth += 1
                    stk.append(i)
                elif i == ')' and stk[-1] == '(':
                    stk.pop()
                    depth -= 1
                else:
                    depth += 1

        return abs(depth)
                


        