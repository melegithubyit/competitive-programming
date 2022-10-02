class Solution(object):
    def compress(self, chars):
        k,inital = 0,0
        while k < len(chars):
            c = chars[k]
            count = 0
            while k < len(chars) and chars[k] == c:
                k += 1
                count += 1
            chars[inital] = c
            inital += 1
            if count > 1:
                for n in list(str(count)):
                    chars[inital] = n
                    inital += 1
        return inital