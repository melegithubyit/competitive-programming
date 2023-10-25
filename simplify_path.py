class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split('/')
        stack = []

        for directory in dir:
            if directory == '.' or directory == '':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        simplified_path = '/' + '/'.join(stack)

        return simplified_path
