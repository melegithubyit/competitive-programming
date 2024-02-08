class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        n = len(nums)
        dis = len(set(nums))
        dic = defaultdict(int)

        left = 0
        right = 0
        count = 0

        while right < n:
            dic[nums[right]] += 1

            while len(dic) == dis:
                dic[nums[left]] -= 1
                if dic[nums[left]] == 0:
                    del dic[nums[left]]

                count += (n - right)
                left += 1
            
            right += 1

        return count

        