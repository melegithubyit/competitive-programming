class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        lst.sort(key = lambda x : int(x[-1]))
        result = ''
        for i in lst:
            result += i.strip(i[-1])
            result += ' '

        return result.strip()

        