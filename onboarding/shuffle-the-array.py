class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        n = len(nums) // 2
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])

        return res
        