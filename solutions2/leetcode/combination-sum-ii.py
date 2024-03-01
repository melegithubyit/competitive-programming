class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(candidates, array):

            if sum(array) == target:
                if array not in result:
                    result.append(array[:])
                return 
            
            elif sum(array) > target:
                return
            
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue 
                    
                array.append(candidates[i])
                backtrack(candidates[i+1:], array)
                array.pop()

        candidates.sort()
        backtrack(candidates, [])

        return result