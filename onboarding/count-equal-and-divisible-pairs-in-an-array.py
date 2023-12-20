class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indices = defaultdict(set)
        counter = 0

        for idx, ele in enumerate(nums):
            if ele not in indices:
                indices[ele].add(idx)
            
            else:
                for i in indices[ele]:
                    if (i * idx) % k == 0:
                        counter += 1
                indices[ele].add(idx)

        return counter