class Solution(object):
    def xorQueries(self,arr,queries):
        list=[]
        for i in range(1,len(arr)):
            arr[i]=arr[i]^arr[i-1]
        for j in queries:
            if j[0]==0:
                list.append(arr[j[1]])
            else:
                list.append(arr[j[1]] ^ arr[j[0]-1])
        return list
