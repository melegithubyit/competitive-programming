class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(' ')
        max_val = float('-inf')

        for i in s:
            max_val = max(max_val, len(i))

        pointer = 0
        res = []

        while pointer < max_val:
            temp = ''

            for i in range(len(s)):
                if len(s[i]) > pointer:
                    temp += s[i][pointer]
                
                else:
                    temp += ' '

            removed_space = temp.rstrip()
            res.append(removed_space)
            pointer += 1

        
        return res
    



        