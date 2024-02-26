class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []

        def backtrack(candidate):

            if len(candidate) == k:
                result.append(candidate[:])
                return 
            

            last = candidate[-1] if candidate else 0
            for i in range(last + 1, n + 1):
                candidate.append(i)
                backtrack(candidate)
                candidate.pop()

        backtrack([])
        return result


        