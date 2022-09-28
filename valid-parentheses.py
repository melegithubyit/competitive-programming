class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i in ["(","{","["]:
                stack.append(i)
            else:
                if not stack:
                    return False
                char=stack.pop()
                if char =='(':
                    if i !=')':
                        return False
                if char =='[':
                    if i !=']':
                        return False
                if char =='{':
                    if i !='}':
                        return False
        if stack:
                return False
        return True