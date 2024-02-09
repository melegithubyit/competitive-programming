class Solution:
    def numberOfWays(self, s: str) -> int:
        splitted = list(s)
        lst = list(map(int, splitted))
        original = lst.copy()

        for i in range(1, len(s)):
            lst[i] += lst[i-1]
        
        zero_count = 0
        zero_lst = []

        for i in splitted:
            if i == '0':
                zero_count += 1
            zero_lst.append(zero_count)

        ans = 0
        for i in range(1, len(s)-1):
            if original[i] == 0:
                one_before = lst[i-1]
                one_after = lst[-1] - lst[i-1]
                num = one_before * one_after
                ans += num
            else:
                zero_before = zero_lst[i-1]
                zero_after = zero_lst[-1] - zero_lst[i-1]
                num = zero_before * zero_after
                ans += num

        return ans

            
            
            




        
        



        