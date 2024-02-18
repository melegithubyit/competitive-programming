class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        openings = {'(','{','['}
        for i in s:
            if i in openings:
                stack.append(i)
            else:
                if stack:
                    popped = stack.pop()
                    if (i == ')' and popped != '(') or (i == '}' and popped != '{') or (i == ']' and popped != '['):
                        return False
                else:
                    return False
        if stack:return False
        return True