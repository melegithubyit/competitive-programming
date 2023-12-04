class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (n + n)

        for i in range(n):
            res[i] = nums[i]
            res[i + n] = nums[i]

        return res
        