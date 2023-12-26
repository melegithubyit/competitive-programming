class Solution(object):
    def sortPeople(self, names, heights):
        new=list(zip(heights,names))
        new.sort(reverse=True)
        output=[]
        for i,j in new:
            output.append(j)
        return output