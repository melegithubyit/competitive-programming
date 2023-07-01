class Solution:
    def arraySortedOrNot(self, arr, n):
        start = 0
        next = 1
        while next != n:
            if arr[next] < arr[start]:
                return False
            next += 1
            start += 1
        return True
