class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        store = dict()
        lst = sorted(nums)
        for idx, ele in enumerate(lst):
            if ele not in store:
                store[ele] = idx

        res = [0] * len(nums)
        for idx,ele in enumerate(nums):
            res[idx] = store[ele]
        
        return res




