class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        input_ = list(map(str, digits))
        number = "".join(input_)
        val = int(number) + 1
        val = str(val)

        incremented = list(val)
        output = list(map(int, incremented))
        return output
        