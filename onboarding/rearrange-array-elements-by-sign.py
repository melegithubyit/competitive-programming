class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_index = 0
        negative_index = 1

        ans = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                ans[positive_index] = nums[i]
                positive_index += 2
            
            else:
                ans[negative_index] = nums[i]
                negative_index += 2

        return ans
            

        

        