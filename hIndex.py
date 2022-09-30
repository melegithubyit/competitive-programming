class Solution:
    def hIndex(self, citations):
            citations.sort()
            h_index = []
            number = len(citations)
            for j,k in enumerate(citations):
                        h_index.append([j,k])

            for i in  h_index:
                    if number-i[0]<=i[1]:
                        return number-i[0]
            return 0
