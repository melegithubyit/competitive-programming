class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        store = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []

        def backtrack(combinations, next_digits):

            if not next_digits:
                result.append(combinations)
                return

            for i in store[next_digits[0]]:
                backtrack(combinations + i, next_digits[1:])

        backtrack("", digits)
        return result


