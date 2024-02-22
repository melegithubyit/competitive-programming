class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        last = len(nums) - 1
        prev = last - 1
        
        while prev >= 0:
            if nums[prev] > nums[last]:
                div = math.ceil(nums[prev] / nums[last])
                res += div - 1
                last -= 1
                nums[last] = (nums[prev] // div)
            else:
                last -= 1
            prev -= 1

        return res


        