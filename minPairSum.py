class Solution(object):
    def minPairSum(self, nums):
        list1=sorted(nums)
        new_list=[]
        n=len(list1)//2
        for i in range(n):
            new_list.append(list1[i]+list1[len(list1)-(i+1)])
        return max(new_list)

