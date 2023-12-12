class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1

        occur = len(arr) // 4

        for i in dic:
            if dic[i] > occur:
                return i

        return 

        