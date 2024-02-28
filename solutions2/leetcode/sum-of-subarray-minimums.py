class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk = [] 
        total = 0 
        n = len(arr)
        for i in range(n + 1): 
            while stk and (i == n or stk[-1][0] > arr[i]): 
                prev_num, prev_index = stk.pop()
                if stk:
                    left = stk[-1][1] 
                else:left = -1 
                total += (prev_index - left) * (i - prev_index) * prev_num 
            if i < n: 
                stk.append([arr[i], i])

        return total % (10 ** 9 + 7)