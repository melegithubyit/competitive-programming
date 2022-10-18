class Solution(object):
    def maxVowels(self, s, k):
        vowels=['a','e','i','o','u']
        counter=0
        inital=list(s)
        out=[]
        for i in range(len(inital)-k+1):
            list=inital[i:i+k]
            for j in list:
                if j in vowels:
                    counter+=1
                out.append(counter)
        return max(out)




















        for i in range(len(inital)):
            if inital[i] in vowels:
                counter+=1


