class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i in range(len(order)):
            dic[order[i]] = i

        left = 0
        right = 1

        while right < len(words):
            w1 = words[left]
            w2 = words[right]

            i = 0
            j = 0

            while i < len(w1) and j < len(w2):
                if dic[w2[j]] > dic[w1[i]]:
                    break

                if dic[w2[j]] < dic[w1[i]]:
                    return False

                i += 1
                j += 1

                if i < len(w1) and j == len(w2):
                    return False

            left += 1
            right += 1

        

        return True
