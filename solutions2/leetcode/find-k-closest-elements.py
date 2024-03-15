class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        for idx, ele in enumerate(arr):
            arr[idx] = [ele, abs(ele - x)]

        arr.sort(key = lambda x: (x[1],x[0]))
        for i in range(k):
            result.append(arr[i][0])
        result.sort()
        return result