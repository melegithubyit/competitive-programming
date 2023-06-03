class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        new_freq = sorted(freq, key=lambda x: freq[x], reverse=True)
        output = ''
        for i in new_freq:
            output += (i * freq[i])
        return output
