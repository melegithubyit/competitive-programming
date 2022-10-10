class Solution:
    def longestOnes(self, nums,k):
        i,j=0,0
        while i < len(nums):
            if nums[i] == 0:
                k -= 1
            i += 1
            if k < 0:
                if nums[j] == 0:
                    k += 1
                j +=1
        return i - j
