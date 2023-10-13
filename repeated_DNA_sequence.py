from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str):
        dic = defaultdict(int)
        n = len(s)
        for i in range(n - 9):
            substring = s[i:i+10]
            dic[substring] += 1

        res = []
        for i in dic:
            if dic[i] > 1:
                res.append(i)

        return res
        
        