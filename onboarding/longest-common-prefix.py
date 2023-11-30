class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        lowest = float('inf')
        for i in strs:
            lowest = min(lowest, len(i))

        counter = 0
        for i in range(lowest):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][counter]:
                    return result

            result += strs[0][i]
            counter += 1

        return result


        




        