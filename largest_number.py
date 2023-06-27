class Solution:
    def largestNumber(self, nums) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        return str(int(''.join(nums)))
