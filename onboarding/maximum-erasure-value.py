class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        current_max_score = 0
        max_score = float('-inf')

        unique = defaultdict(int)

        left = 0

        for right in range(len(nums)):
            unique[nums[right]] += 1

            while len(unique) != right - left + 1:
                current_max_score -= nums[left]
                max_score = max(max_score, current_max_score)
                unique[nums[left]] -= 1
                if unique[nums[left]] == 0:
                    del unique[nums[left]]
                left += 1


            current_max_score += nums[right]
            max_score = max(max_score, current_max_score)

        return max_score
                
                

