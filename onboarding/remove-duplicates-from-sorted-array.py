class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        elements = set()
        elements.add(nums[0])
        n = len(nums)
        left = 1
        right = 1

        while left < len(nums):

            while right < len(nums) and nums[right] in elements:
                right += 1
            if right < len(nums):
                nums[left] = nums[right]
                elements.add(nums[right])
                left += 1
            if right >= len(nums):break
            
        
        for i in range(left, n):
            nums[i] = None

        
        return left


















