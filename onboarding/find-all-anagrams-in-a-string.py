class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return ""


        target = defaultdict(int)
        for i in p:
            target[i] += 1
        
        store = defaultdict(int)
        for i in range(len(p)):
            store[s[i]] += 1
        
        ans = []
        left = 0
        right = len(p)

        if store == target:
            ans.append(left)
        
        while right < len(s):
            store[s[right]] += 1
            store[s[left]] -= 1
            if store[s[left]] == 0:
                del store[s[left]]

            left += 1
            

            if store == target:
                ans.append(left)

            right += 1
        
        return ans

        

        