class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        length = len(nums)
        min_add = nums[0] + nums[1] + nums[2]
        if length == 3:
            return sum(nums)
        else:
            nums.sort()
            for i in range(length - 2):
                j = i + 1
                k = length-1
                while j < k:
                    added =  nums[i] + nums[j] + nums[k]
                    if abs(added - target) < abs(min_add - target):
                        min_add = added
                    if added == target:
                        return added
                    elif added > target:
                        k -= 1
                    else:
                        j += 1
        return min_add








