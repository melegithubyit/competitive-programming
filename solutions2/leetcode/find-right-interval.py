class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        store = {}
        arr = []
        for idx, ele in enumerate(intervals):
            arr.append(ele[0])
            store[ele[0]] = idx
        
        arr.sort()
        # arr = [1,2,3]
        
        def binary_search(number, arr):
            left = 0
            right = len(arr) - 1

            while left < right:
                mid = (left + right) // 2
                if arr[mid] < number:
                    left = mid + 1
                else:
                    right = mid
            
            return arr[left]
        
        result = []
        for i in intervals:
            _, num = i
            if binary_search(num, arr) >= num:
                result.append(store[binary_search(num, arr)])
            else:
                result.append(-1)
        
        return result

