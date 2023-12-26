class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashT = Counter(arr1)
        res = []
        temp = []

        for i in arr2:
            for _ in range(hashT[i]):
                res.append(i)
            del hashT[i]

        for i in hashT:
            for _ in range(hashT[i]):
                temp.append(i)

        temp.sort()

        res.extend(temp)
        return res
        