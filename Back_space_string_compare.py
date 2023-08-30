class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def createString(strVal):
            result = []
            for i in strVal:
                if i != '#':
                    result.append(i)
                else:
                    if result:
                        result.pop()
            return result
        return createString(s) == createString(t)
