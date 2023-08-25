from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        counter = Counter(tasks)
        frequency = sorted(list(counter.values()))

        i = frequency.pop()
        total = (i-1)*n

        while frequency and total > 0:
            total = total-min(i-1, frequency.pop())

        total = max(0, total)
        return len(tasks) + total
