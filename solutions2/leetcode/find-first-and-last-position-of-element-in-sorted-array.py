class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        result = [-1, -1]
        frontFlag = False
        backFlag = False

        left = 0
        right = len(nums) - 1

        while left <= right:
            if frontFlag and backFlag:
                return result

            else:
                if nums[left] == target:
                    result[0] = left
                    frontFlag = True
                else:
                    left += 1
                
                if nums[right] == target:
                    result[1] = right
                    backFlag = True
                else:
                    right -= 1

        return result