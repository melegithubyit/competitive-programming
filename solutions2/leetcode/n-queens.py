class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        state = []
        self.backtrack(state, result, n)
        return result

    
    def is_valid_state(self, state, n):
        return len(state) == n
    
    def get_candidates(self, state, n):
        if not state:
            return range(n)
        
        position = len(state)
        candidates = set(range(n))
        for row, col in enumerate(state):
            candidates.discard(col)
            distance = position - row

            candidates.discard(col + distance)
            candidates.discard(col - distance)

        return candidates

    def backtrack(self, state, result, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            result.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.backtrack(state, result, n)
            state.pop()

    def state_to_string(self, state, n):
        res = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            res.append(string)

        return res



        
            