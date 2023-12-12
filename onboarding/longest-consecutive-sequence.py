class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        Set = set(nums)
        longest_seq = 0

        for i in nums:
            if i - 1 not in Set:
                length = 0
                while i + length in Set:
                    length += 1
                
                longest_seq = max(longest_seq, length)

        return longest_seq

        