class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        for i in range((num//3) - 3, num // 3):
            if (3 * i) + 3 == num:
                return [i, i+1, i+2]

        return []

        