class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1

        return arr[left:right + 1]
