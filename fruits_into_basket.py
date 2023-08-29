class Solution:
    def totalFruit(self, fruits):
        max_fruits = 0
        count = {}
        start = 0

        for end in range(len(fruits)):
            count[fruits[end]] = count.get(fruits[end], 0) + 1

            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    del count[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits
