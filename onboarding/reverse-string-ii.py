class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        for i in range(0, len(s), k+k):
            substring = s[i : i+(2*k)]
            res += substring[0:k][::-1]+substring[k:] 
        return res