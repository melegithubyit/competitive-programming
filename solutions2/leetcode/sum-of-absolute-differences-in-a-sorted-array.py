class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        original = nums.copy()
        result = []

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        def compute(index, ele, nums):
            if index > 0:
                left_sum = (ele * index) - nums[index-1]
            else: left_sum = (ele * index)
            right_sum = total - nums[index] - (ele * (n - index - 1))
            return left_sum + right_sum

        for idx, ele in enumerate(original):
            number = compute(idx, ele, nums)
            result.append(number)

        return result




        