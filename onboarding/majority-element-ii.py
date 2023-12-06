class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums) // 3
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        
        res= []
        for i in nums:
            if dic[i] > freq and i not in res:
                res.append(i)
            
        return res

        