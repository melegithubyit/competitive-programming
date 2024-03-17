class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search1(arr, tagret):
            left = 0
            right = len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid][0] <= target and arr[mid][-1] >= target:
                    return arr[mid]
                elif arr[mid][0] > target:
                    right = mid
                elif arr[mid][-1] < target:
                    left = mid + 1 
            return arr[left]
        
        def binary_search2(arr, target):
            index = bisect.bisect_right(arr, target)
            if arr[index - 1] == target:
                return True
            return False
        
        lst = binary_search1(matrix, target)
        return binary_search2(lst, target)