class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        one_count = 0
        for i in s:
            if i == '1':
                one_count += 1
            else:
                result += one_count

        return result
