class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""

        target = Counter(t)
        left = 0
        res_length = float('inf')
        store = defaultdict(int)
        have = 0
        need = len(target)
        result = [-1, -1]

        for right in range(len(s)):
            store[s[right]] += 1
            if s[right] in target and store[s[right]] == target[s[right]]:
                have += 1

            while have == need:
                
                if (right - left + 1) < res_length:
                    result = [left, right]
                    res_length = (right - left + 1)

                store[s[left]] -= 1
                if store[s[left]] == 0:
                    del store[s[left]]
                 
                if s[left] in target and store[s[left]] < target[s[left]]:
                    have -= 1

                left += 1

        start, end = result
        return s[start:end + 1] if result != float("inf") else ""

        
        
        
                
        