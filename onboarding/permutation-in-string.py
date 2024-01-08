class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        store = Counter(s2[:len(s1)])
        if target == store:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            store[s2[right]] += 1
            store[s2[left]] -= 1
            if store[s2[left]] == 0:
                del store[s2[left]]
            
            left += 1
            if store == target:
                return True

        return False


        