class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        inital = [0] * n

        for i in shifts:
            left, right, ele = i

            if ele == 1:
                inital[left] += 1
                if right < len(s) - 1:
                    inital[right + 1] -= 1
            
            else:
                inital[left] -= 1
                if right < len(s) - 1:
                    inital[right + 1] += 1
        
        for i in range(1, len(inital)):
            inital[i] += inital[i-1]
        
        print(inital)

        res = ''

        for i in range(n):
            if inital[i] < 0:
                inital[i] += 26
            res += chr(((ord(s[i]) - 97 + inital[i]) % 26) + 97)

        return res


        