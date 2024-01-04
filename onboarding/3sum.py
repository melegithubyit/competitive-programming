class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):

            if nums[i] == nums[i-1] and i > 0:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                _sum = nums[left] + nums[right] + nums[i]
                if _sum > 0:
                    right -= 1
                elif _sum < 0:
                    left += 1

                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result

        