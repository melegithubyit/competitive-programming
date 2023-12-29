class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        # print(str(5)>str(34343))
        return str(int(''.join(nums)))