class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        idx = 0
        flag = False
        check = False

        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                idx = i
                check = True
                break
        
        if check:
            for i in range(idx):
                if arr[i+1] <= arr[i]:
                    flag = True
            
            for i in range(idx, len(arr) - 1):
                if arr[i] <= arr[i+1]:
                    flag = True

            if flag:
                return False
            return True
        else:
            return False


        