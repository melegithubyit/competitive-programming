class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = path.split('/')
        print(splitted)
        stack = []

        for char in splitted:
            if char == '.' or char == '':
                continue
            elif char == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        print(stack)
        return '/' + ('/'.join(stack))