class Solution(object):
    def targetIndices(self, nums, target):
        output=[]
        for i in range(0, len(nums) - 1):
            current_min_index = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[current_min_index]:
                    current_min_index = j
            nums[i], nums[current_min_index] = nums[current_min_index], nums[i]
        list=nums
        for i in range(len(list)):
            if list[i]==target:
                output.append(i)
        return output

trial=Solution()
nums=[1,2,5,2,3]
print(trial.targetIndices(nums,2))