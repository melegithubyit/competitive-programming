class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        fewq = n // 4
        store = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}

        for char in s:
            store[char] += 1

        if all(count == fewq for count in store.values()):
            return 0

        min_len = float('inf')
        left = 0

        for right in range(n):
            store[s[right]] -= 1

            while all(count <= fewq for count in store.values()):
                min_len = min(min_len, right - left + 1)
                store[s[left]] += 1
                left += 1

        return min_len