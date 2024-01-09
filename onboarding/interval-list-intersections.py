class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        left = 0
        right = 0

        while left < len(firstList) and right < len(secondList):
            f_str, f_end = firstList[left]
            s_str, s_end = secondList[right]

            max_val = max(f_str, s_str)
            min_val = min(f_end, s_end)

            if max_val <= min_val:
                ans.append([max_val, min_val])
            
            if s_end >= f_end:
                left += 1
            else:
                right += 1

        return ans
        