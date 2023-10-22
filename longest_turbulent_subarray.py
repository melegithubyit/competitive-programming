class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        n = len(arr)
        data = [0]*(n-1)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                data[i] = 1
            if arr[i] < arr[i+1]:
                data[i] = -1
        if data == [0]*(n-1):
            return 1
        left = 0
        right = 0
        max_len = 0
        while left < n-1:
            while right < n-2:
                if data[right] * data[right+1] < 0:
                    right += 1
                else:
                    break
            if right-left+1 > max_len:
                max_len = right-left+1
            right += 1
            left = right
        return max_len+1
