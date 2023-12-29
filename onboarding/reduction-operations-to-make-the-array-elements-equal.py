class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        tracker = list(set(nums))
        tracker.sort(reverse = True)
        counter = Counter(nums)

        operations = 0
        mid_val = 0

        for i in range(len(tracker) - 1):
            value = counter[tracker[i]]
            operations += (value + mid_val)
            mid_val += value
        
        return operations






































        