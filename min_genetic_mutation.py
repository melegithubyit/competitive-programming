from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene}
        while queue:
            curr, dist = queue.popleft()
            if curr == endGene:
                return dist
            for i in range(len(curr)):
                for c in 'ACGT':
                    new = curr[:i] + c + curr[i+1:]
                    if new in bank and new not in visited:
                        queue.append((new, dist+1))
                        visited.add(new)
        return -1