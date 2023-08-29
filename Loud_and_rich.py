class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = [[] for _ in range(n)]
        result = [-1] * n
        for u, v in richer:
            graph[v].append(u)

        def dfs(person):
            if result[person] >= 0:
                return result[person]
            result[person] = person
            for neighbor in graph[person]:
                if quiet[result[person]] > quiet[dfs(neighbor)]:
                    result[person] = result[neighbor]
            return result[person]
        for i in range(n):
            dfs(i)
        return result
