class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ''
        counter = 0
        index = 0
        for i in range(len(s)):
            if index < len(spaces):
                if counter == spaces[index]:
                    res += ' '
                    index += 1

            res += s[i]
            counter += 1

        return res

        