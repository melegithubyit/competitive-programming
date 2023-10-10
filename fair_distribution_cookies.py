class Solution:
    def distributeCookies(self, cookies, k: int) -> int:
        lst = [0] * k
        self.s = float('inf')

        def helper(lst, i):
            if i >= len(cookies):
                self.s = min(self.s, max(lst))
                return
            if max(lst) >= self.s:
                return
            for j in range(k):
                lst[j] += cookies[i]
                helper(lst, i+1)
                lst[j] -= cookies[i]

        helper(lst, 0)
        return self.s
