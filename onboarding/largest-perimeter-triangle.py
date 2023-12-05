class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        def isValid(lst:list) -> bool:
            if lst[0] + lst[1] > lst[2] and lst[0] + lst[2] > lst[1] and lst[1] + lst[2] > lst[0]:
                return True
            return False

        n = len(nums)
        max_val = 0
        for i in range(n - 3 + 1):
            temp = nums[i:i+3]
            if isValid(temp):
                max_val = max(max_val, sum(temp))
        
        return max_val

        