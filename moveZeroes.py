class Solution:
    def moveZeroes(self, nums):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==0 and nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    break

        return nums
trial=Solution()
nums=[0,1,0,12,3]
print(trial.moveZeroes(nums))