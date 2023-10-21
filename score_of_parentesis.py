class Solution(object):
    def scoreOfParentheses(self, s):

        ans = 0
        depth = 0
        for idx, cr in enumerate(s):

            if cr == '(':
                depth += 1
            else:
                depth -= 1
                if s[idx-1] == '(':
                    ans += 2**depth

        return ans
