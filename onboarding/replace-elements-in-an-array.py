class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = dict()

        for idx, ele in enumerate(nums):
            dic[ele] = idx
        
        for s, e in operations:
            idx = dic[s]
            nums[idx] = e
            dic[e] = idx
        
        return nums
        