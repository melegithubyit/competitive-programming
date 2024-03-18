class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def is_valid(nums, number, threshold):
            counter = 0
            for i in nums:
                counter += math.ceil(i / number)
            return counter <= threshold
        
        samples = [i for i in range(1, max(nums) + 1)]
        min_val = float('inf')
        Flag = False
        left = 0
        right = len(samples)

        while left < right:
            mid = (left + right) // 2
            value = samples[mid]
            if is_valid(nums, value, threshold):
                min_val = value
                Flag = True
                right = mid
            else:
                left = mid + 1
        
        if Flag:
            return min_val
        return left
