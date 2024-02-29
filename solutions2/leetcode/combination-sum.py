class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(candidates, targett, pre, lst):
            if pre == target:
                result.append(sorted(lst.copy()))
            
            if pre > target:
                return
            
            for i in candidates:
                lst.append(i)
                backtrack(candidates, target, pre + i, lst)
                lst.pop()
        
        backtrack(candidates, target, 0, [])
        
        n = len(result)
        ans = []
        
        for i in range(n):
            if result[i] in ans:
                continue

            ans.append(result[i])

        return ans