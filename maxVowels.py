class Solution(object):
    def maxVowels(self, s, k):
        vowels=['a','e','i','o','u']
        inital=list(s)
        out=[]
        for i in range(len(inital)-k+1):
            list1=inital[i:i+k]
            counter = 0
            for j in range(len(list1)):
                if list1[j] in vowels:
                    counter+=1
            out.append(counter)
        return max(out)



















        for i in range(len(inital)):
            if inital[i] in vowels:
                counter+=1


