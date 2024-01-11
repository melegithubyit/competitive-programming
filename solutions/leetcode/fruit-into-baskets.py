class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 2:
            return 2
        store = Counter(fruits[:2])

        left = 0
        max_picked = len(store)

        for right in range(2, len(fruits)):

            store[fruits[right]] += 1

            while left <= right and len(store) > 2:
                store[fruits[left]] -= 1
                if store[fruits[left]] == 0:
                    del store[fruits[left]]

                left += 1

            max_picked = max(max_picked, right - left  + 1)
        
        return max_picked


        