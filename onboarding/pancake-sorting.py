class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(end):
            start = 0
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        N = len(arr)
        result = []
        for i in range(N-1, -1, -1):
            max_val = i
            for j in range(i, -1, -1):
                if arr[j] > arr[max_val]:
                    max_val = j
            if max_val != i:
                flip(max_val)
                flip(i)
                result.append(max_val + 1)
                result.append(i + 1)
        return result


            











        