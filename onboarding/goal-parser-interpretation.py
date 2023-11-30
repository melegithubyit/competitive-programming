class Solution:
    def interpret(self, command: str) -> str:
        res = ''
        left = 0
        while left < len(command):
            if command[left] == 'G':
                res += 'G'
                left += 1
            
            elif command[left] == '(' and command[left + 1] == ')':
                res += 'o'
                left += 2

            else:
                res += 'al'
                left += 4

        return res



        
        