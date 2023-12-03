class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def NumberToString(value : int) -> str:
            temp = ''
            while value:
                rem = value % 10
                value //= 10
                temp += chr(rem + ord('0'))

            return temp[::-1]

        
        
        def StringToNumber(value : str) -> int:
            x = 0
            for i in value:
                x = (10 * x) + (ord(i) - ord('0'))
            
            return x


        answer = NumberToString(StringToNumber(num1) * StringToNumber(num2))
        if answer:
            return answer
        
        else:
            return '0'
        