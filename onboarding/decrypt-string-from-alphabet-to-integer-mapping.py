class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {}
        for i in range(97, 123):
            if i - 96 < 10:
                dic[str(i-96)] = chr(i)
            else:
                dic[(str(i - 96) + '#')] = chr(i)


        result = ''
        pointer = 0
        
        while pointer < len(s):
            if pointer <= len(s) - 3:
                if s[pointer:pointer+3] in dic:
                    result += dic[s[pointer:pointer+3]]
                    pointer += 3
                
                else:
                    result += dic[s[pointer]]
                    pointer += 1

            else:
                result += dic[s[pointer]] 
                pointer += 1


        return result



