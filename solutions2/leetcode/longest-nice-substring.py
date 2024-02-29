class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def helper(string):
            dic = set(string)
            if len(string) < 2:
                return ""
            
            for i in range(len(string)):
                if not (string[i].lower() in dic and string[i].upper() in dic):
                    string1 = helper(string[:i])
                    string2 = helper(string[i+1:])
                    return string2 if len(string2) > len(string1) else string1

            return string
        
        return helper(s)




