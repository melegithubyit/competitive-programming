class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dictionary = { 'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        after = [['V','X'], ['L','C'],['D','M']]
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                if s[i] == 'I' and s[i+1] not in after[0]:
                    result += dictionary['I']
                    i += 1
                elif s[i] == 'I' and s[i+1] in after[0]:
                    result += (dictionary[s[i+1]] - dictionary[s[i]])
                    i += 2
            
                elif s[i] == 'X' and s[i+1] not in after[1]:
                    result += dictionary['X']
                    i += 1
                elif s[i] == 'X' and s[i+1] in after[1]:
                    result += (dictionary[s[i+1]] - dictionary[s[i]])
                    i += 2

                elif s[i] == 'C' and s[i+1] not in after[2]:
                    result += dictionary['C']
                    i += 1
                elif s[i] == 'C' and s[i+1] in after[2]:
                    result += (dictionary[s[i+1]] - dictionary[s[i]])
                    i += 2

                else:
                    result += dictionary[s[i]]
                    i += 1

            else:
                result += dictionary[s[i]]
                i += 1

        return result
            


            

            

                



