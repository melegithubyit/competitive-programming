class Solution(object):
    def sortSentence(self, s):
        arr = s.split(" ")
        sorted = ''
        for i in range(1,len(arr)+1):
            for j in arr:
                if int(j[-1])== i:
                    sorted += j[:len(j)-1] + ' '
        return sorted[: -1]