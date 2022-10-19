from collections import Counter
class Solution:
    def minSetSize(self, arr):
        freq = list(Counter(arr).items())
        n = len(arr)//2
        freq.sort(key=lambda x: x[1])
        print(freq)
        sum = 0
        for i in range(len(freq)-1,-1,-1):
            sum += freq[i][1]
            if sum >= n:
                return len(freq) - i

