class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiopQWERTYUIOP")
        secondRow = set("asdfghjklASDFGHJKL")
        thirdRow = set("zxcvbnmZXCVBNM")

        result = []
        for i in words:
            set_value = set(i)
            if set_value.issubset(firstRow) or set_value.issubset(secondRow) or set_value.issubset(thirdRow):
                result.append(i)

        return result 



        