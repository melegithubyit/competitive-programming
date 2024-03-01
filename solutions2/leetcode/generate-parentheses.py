class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        def backtrack(string, opening, closing):
            
            if opening == 0 and closing == 0:
                result.append(string)
                return
            
            if opening == closing and opening != 0:
                string += "("
                backtrack(string, opening - 1, closing)

            elif opening < closing and opening > 0:
                string += "("
                backtrack(string, opening - 1, closing)
                string = string[:-1]
                string += ")"
                backtrack(string, opening, closing - 1)


            elif opening == 0 and closing:
                string += ")"
                backtrack(string, opening, closing - 1)


        backtrack("", n, n)
        return result
            

            

            
