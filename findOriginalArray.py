class Solution(object):
    def findOriginalArray(self, changed):
        list=[]
        for i in range(0,len(changed)):
            for j in range(i+1,len(changed)):
                if changed[j]==2*changed[i]:
                    list.append(changed[i])

        return list
