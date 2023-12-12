class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        current_even_sum = 0
        for i in nums:
            if i % 2 == 0:
                current_even_sum += i

        res = []
        for i in queries:
            val, index = i
            new_val = nums[index] + val
            if new_val % 2 == 0 and nums[index] % 2 == 0:
                current_even_sum += val
            
            elif new_val % 2 == 1 and nums[index] % 2 == 0:
                current_even_sum -= nums[index]
            
            elif new_val % 2 == 0 and nums[index] % 2 == 1:
                current_even_sum += new_val

            res.append(current_even_sum)
            nums[index] = new_val

        return res