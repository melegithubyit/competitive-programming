class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        pt1 = 0
        pt2 = 0

        ans = 0

        while pt1 < len(g) and pt2 < len(s):
            if s[pt2] >= g[pt1]:
                ans += 1
                pt1 += 1
                pt2 += 1
            
            elif s[pt2] < g[pt1]:
                pt2 += 1
        
        return ans
        